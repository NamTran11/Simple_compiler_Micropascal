.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static max(III)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
.var 3 is max I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	iload_2
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iload_0
	istore_3
	goto Label9
Label8:
	iload_2
	istore_3
Label9:
	goto Label5
Label4:
	iload_1
	iload_2
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	iload_1
	istore_3
	goto Label13
Label12:
	iload_2
	istore_3
Label13:
Label5:
	iload_3
	ireturn
Label1:
.limit stack 2
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label3
.var 2 is b I from Label2 to Label3
.var 3 is c I from Label2 to Label3
.var 4 is d Z from Label2 to Label3
Label2:
	sipush 500
	istore_1
	bipush 100
	istore_3
	iload_3
	istore_2
	iload_3
	iload_2
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore 4
	iload_1
	iload_2
	iload_3
	invokestatic MPClass/max(III)I
	invokestatic io/putInt(I)V
	iload 4
	iload_1
	iload_3
	iload_2
	invokestatic MPClass/max(III)I
	iload_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ifle Label8
	iload 4
	invokestatic io/putBool(Z)V
Label8:
Label3:
Label1:
	return
.limit stack 4
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
