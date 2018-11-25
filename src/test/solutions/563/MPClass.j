.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static UCLN(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
Label2:
	iload_0
	iload_1
	if_icmpeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_0
	iload_1
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iload_0
	iload_1
	isub
	istore_0
	goto Label9
Label8:
	iload_1
	iload_0
	isub
	istore_1
Label9:
	goto Label2
Label3:
	iload_0
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label3
.var 2 is b I from Label2 to Label3
.var 3 is c I from Label2 to Label3
.var 4 is d Z from Label2 to Label3
Label2:
	bipush 8
	istore_1
	iconst_4
	istore_2
	iload_1
	iload_2
	invokestatic MPClass/UCLN(II)I
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
