def add(num1,num2):
	return num1+num2
def substract(num1,num2):
	return num1-num2
def multiply(num1,num2):
	return num1*num2
def divide(num1,num2):
	if num2==0:
		print("division is not possible")
	else: 
		return num1/num2
def power(num1,num2):
	return num1**num2
def calculator(num1,oper,num2):
	if oper=="+":
		return add(num1,num2)
	elif oper=="-":
		return substract(num1,num2)
	elif oper=="*":
		return multiply(num1,num2)
	elif oper=="/":
		return divide(num1,num2)
	elif oper=="**":
		return power(num1,num2)
	else:
		print("invalid choice>>>")
num1=int(input("enter the first number:  "))
num2=int(input("enter the second number: "))
oper=input("enter the operator:")
result=calculator(num1,oper,num2)
print(result)
		
