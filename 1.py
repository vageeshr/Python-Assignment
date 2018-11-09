def add(x,y):
	return  x+y;
def sub(x,y):
	return x-y;

def mul(x,y):
	return x*y;

def div(x,y):
	return x/y;
def mod(x,y):
	return x%y;
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
choice=input("select opertion :")

if (choice =='+'):
	print("sum is ",add(a,b))

elif (choice =='-'):
	print("sub is ",sub(a,b))

elif (choice =='*'):
	print("mul is ",mul(a,b))

elif (choice =='/'):
	print("div is ",div(a,b))
else:
	print("modulus is",mod(a,b))
