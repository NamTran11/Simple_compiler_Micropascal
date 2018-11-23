'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
import functools

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [    Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName)),
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def VarGlobal(self, ast, c):
        ctxt = c
        nameAtt = ast.variable.name
        typeAtt = ast.varType
        self.emit.printout(self.emit.emitATTRIBUTE(nameAtt, typeAtt, False, ""))
        symbol = Symbol(ast.variable.name, typeAtt, CName(self.className))
        c.append(symbol)
        return c

    def FuncGlobal(self,ast, c):
        ctxt = c
        nameFunc = ast.name.name
        typeFunc = MType([x.varType for x in ast.param], ast.returnType)
        symbol = Symbol(nameFunc, typeFunc, CName(self.className))
        c.append(symbol)
        return c

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        nenv = functools.reduce(lambda x,y: self.VarGlobal(y,x) if type(y) is VarDecl else self.FuncGlobal(y,x), ast.decl, self.env if self.env else []) 

        e = SubBody(None, nenv)
        lsFun = list(filter(lambda x:type(x) is FuncDecl, ast.decl))
        for x in lsFun:
            e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        glSubBody = SubBody(frame,glenv)
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            glSubBody = functools.reduce(lambda a,b: self.visit(b,a), consdecl.param, glSubBody) 

        body = consdecl.body

        current_env = functools.reduce(lambda a,b: self.visit(b,a), consdecl.local, glSubBody)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        #visit body of function
        list(map(lambda x: self.printoutStmt(x, current_env), body))

        # get and print Endlabel
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def printoutStmt(self,ast,env):
        #env    : SubBody
        frame  = env.frame
        newEnv = env.sym
        if type(ast) is Assign:
            self.emit.printout(self.visit(ast, Access(frame, newEnv, True, True))[0])

        elif type(ast) is CallExpr:
            self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True))[0])
            sym = self.lookup(ast.method.name, newEnv, lambda x:x.name) 
            returnType = sym.mtype.rettype

            if type(returnType) != VoidType:
                self.emit.printout(self.emit.emitPOP(frame))

        elif type(ast) in [UnaryOp,BinaryOp,Id,IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:        
                self.emit.printout(self.visit(ast, Access(frame, newEnv, False, True))[0])
                self.emit.printout(self.emit.emitPOP(frame))
        elif type(ast) in [If,For,While,Break,Continue,With,CallStmt]:
            self.visit(ast, env)

    def visitVarDecl(self,ast,c):
        #ast: VarDecl
        #c  : SubBody
        env  = c.sym if type(c) is SubBody else []
        indx = c.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(indx, ast.variable.name, ast.varType, c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
        return SubBody(c.frame, [Symbol(ast.variable.name, ast.varType, Index(indx))] + env)

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        #self.curFunc = self.lookup(ast.name.name, subctxt.sym, lambda x: x.name)
        self.genMETHOD(ast, subctxt.sym, frame)
        return o
        #return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitAssign(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym

        (resLeft1, typeLeft1) = self.visit(ast.lhs, Access(frame, env, True, True))
        (resRight, typeRight) = self.visit(ast.exp,Access(frame, env, False, True))

        str_I2f = self.emit.emitI2F(frame) if (type(typeLeft1),type(typeRight)) == (FloatType,IntType) else ""

        (resLeft2, typeLeft2) = self.visit(ast.lhs, Access(frame, env, True, False))
        
        op_Str = resLeft1 + resRight + str_I2f  + resLeft2

        return op_Str,typeLeft1

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBinaryOp(self,ast,o):

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        str1, type1 = self.visit(ast.left,Access(frame, nenv, False, True))
        str2, type2 = self.visit(ast.right,Access(frame, nenv, False, True))
        retType = type1
        if (type(type1) ,type(type2)) == (FloatType,IntType):
            str2+=self.emit.emitI2F(frame)
            retType = FloatType()
        elif (type(type1) ,type(type2)) == (IntType,FloatType):
            str1+=self.emit.emitI2F(frame)
            retType = FloatType()
        elif (type(type1) ,type(type2)) == (IntType,IntType):
            if ast.op is '/':
                str2+=self.emit.emitI2F(frame)
                str1+=self.emit.emitI2F(frame)
                retType = FloatType()
            else:
                retType = IntType()

        if ast.op in ['+','-']:
            return str1+str2+self.emit.emitADDOP(ast.op,retType,frame),retType
        elif ast.op in ['*','/']:
            return str1+str2+self.emit.emitMULOP(ast.op,retType,frame),retType
        elif ast.op == 'mod': # error ,let fix as soon as posible
            return str1+str2+self.emit.emitMOD(frame),IntType()
        elif ast.op == 'div':
            return str1+str2+self.emit.emitDIV(frame),IntType()
        elif ast.op in ['<','>','<=','>=','=','<>']:
            return str1+str2+self.emit.emitREOP(str(ast.op), retType, frame),BoolType()
            # emiter line 421 có lỗi
        elif ast.op in ['and','or']:
            pass
        elif ast.op in ['anthen','orelse']:
            pass

    def visitUnaryOp(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym
        resExpr, typeExpr = self.visit(ast.body, Access(frame, env, False, True))
        if ast.op == "not":
            return resExpr + self.emit.emitNOT(typeExpr, frame), typeExpr
        elif ast.op == "-": 
            return resExpr + self.emit.emitNEGOP(typeExpr, frame), typeExpr

    def visitId(self,ast,o):
        # o : Access (co the la SubBody)
        if type(o) != SubBody: 

            sym  = self.lookup(ast.name, o.sym, lambda x: x.name)
            code = ""

            if (o.isLeft,o.isFirst) == (True, True):
                pass
            elif (o.isLeft,o.isFirst) == (True, False):

                if type(sym.value) is CName:
                    code = self.emit.emitPUTSTATIC(sym.value.value + "." + ast.name, sym.mtype, o.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o.frame)

            elif o.isLeft == False:
                if type(sym.value) is CName:
                    code = self.emit.emitGETSTATIC(sym.value.value + "." + ast.name, sym.mtype, o.frame)
                elif type(sym.value) is Index:
                    code = self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o.frame)

            return code,sym.mtype

        else:
            sym  = self.lookup(ast.name, o.sym, lambda x: x.name)
            return "",sym.mtype

    def visitStringLiteral(self, ast, o):
        #ast: StringLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(str(ast.value), StringType(), frame), StringType()

    def visitBooleanLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()
    