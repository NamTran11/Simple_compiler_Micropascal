.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static fact(II)I
.var 0 is x I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
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
	iload_0
	iload_0
	iload_1
	iconst_1
	isub
	invokestatic MPClass/fact(II)I
	imul
	ireturn
Label5:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	iconst_3
	invokestatic MPClass/fact(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
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
