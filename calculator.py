def sum(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b

op=input("Which operator (+) or (-) or (*) or (/) ? ")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

add=sum(a,b)
substract=sub(a,b)
multiply=mul(a,b)
divide=div(a,b)


if op=='+':
 	print(a,"+",b,' is ',add)
elif op=='-':
 	print(a,"-",b,' is ', substract)
elif op=='*':
 	print(a,"*",b,' is ',multiply)
elif op=='/':
 	print(a,"/",b,' is ', divide)
else:
 	print("Operator not defined ! ")
