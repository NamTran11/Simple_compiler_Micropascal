.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static cmp(II)Z
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iconst_5
	isub
	iload_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
	goto Label5
Label4:
	iconst_0
	ireturn
Label5:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	bipush 8
	istore_1
	iconst_2
	istore_2
	iload_1
	iload_2
	invokestatic MPClass/cmp(II)Z
	ifle Label2
	iload_1
	invokestatic io/putInt(I)V
	goto Label3
Label2:
	iload_2
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
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
