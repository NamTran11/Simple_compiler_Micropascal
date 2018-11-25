.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static tong(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static square(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iload_0
	imul
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static sub(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_0
	iload_1
	isub
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	invokestatic MPClass/sub(II)I
	iconst_1
	iconst_2
	invokestatic MPClass/tong(II)I
	imul
	invokestatic MPClass/square(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 1
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
