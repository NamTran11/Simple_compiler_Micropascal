.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static fibonaci(I)I
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
	iconst_1
	ireturn
	goto Label5
Label4:
	iload_0
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iconst_1
	ireturn
	goto Label9
Label8:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/fibonaci(I)I
	iload_0
	iconst_2
	isub
	invokestatic MPClass/fibonaci(I)I
	iadd
	ireturn
Label9:
Label5:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	invokestatic MPClass/fibonaci(I)I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
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
