.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MPClass.x I
Label2:
	getstatic MPClass.x I
	iconst_0
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label4
	getstatic MPClass.x I
	invokestatic io/putInt(I)V
Label3:
	getstatic MPClass.x I
	iconst_1
	isub
	putstatic MPClass.x I
	goto Label2
Label4:
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
