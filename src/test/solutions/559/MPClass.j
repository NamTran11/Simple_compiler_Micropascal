.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static tong_n(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	ireturn
Label4:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MPClass/tong_n(I)I
	iadd
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	bipush 10
	istore_1
	iload_1
	invokestatic MPClass/tong_n(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
