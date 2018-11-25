.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static f()I
Label0:
	iconst_2
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
.var 2 is y F from Label0 to Label1
Label0:
.var 3 is x I from Label2 to Label3
.var 4 is y I from Label2 to Label3
Label2:
	iconst_5
	istore 4
	iload 4
	istore_3
Label4:
	iload_3
	bipush 100
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
	iload_3
	bipush 100
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	goto Label6
	goto Label12
Label11:
	iload_3
	bipush 50
	iadd
	istore_3
Label12:
Label5:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label6:
	iload_3
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 2
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
