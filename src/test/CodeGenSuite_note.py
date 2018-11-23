import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_00(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_1(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putInt"),[IntLiteral(5)])])])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_2(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(100.0); end"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_3(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(100.0); end"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_4(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(10+2); end"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_5(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10.0+2.0); end"""
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_6(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10+2.0); end"""
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_7(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10*2.0); end"""
        expect = "20.0"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_8(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(10-2.0); end"""
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_9(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(2.0-10); end"""
        expect = "-8.0"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_10(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(2.0-10+10); end"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_11(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(2.0 / 10.0); end"""
        expect = "0.2"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_12(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(4+2/2); end"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_13(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100 div 2); end"""
        expect = "50"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_14(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putBool(true); end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_15(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(-9); end"""
        expect = "-9"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_16(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(-9.5); end"""
        expect = "-9.5"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_17(self):
        """Simple program: int main() {} """
        input = """
        //var x:integer;
        procedure main();
        begin 
            putString("Hello World"); 
        end"""
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_18(self):
        """Simple program: int main() {} """
        input = """
        //var x:integer;
        procedure main();
        begin 
            putBool(not false); 
        end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_19(self):
        """Simple program: int main() {} """
        input = """
        //var x:integer;
        procedure main();
        begin 
            putInt(1 mod 2); 
        end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,519))

