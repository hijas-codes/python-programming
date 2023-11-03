num1=float(input("Enter the first Number:"))
num2=float(input("Enter the second Number:"))
operation=input("select the opration(+,-,*,/,%,**,//):")
if operation=="+":
	result=num1+num2
elif operation=="-":
	result=num1-num2
elif operation=="*":
	result=num1*num2
elif operation=="/":
	result=num1/num2
elif operation=="%":
	result=num1%num2
elif operation=="**":
	result=num1**num2
elif operation=="//":
	result=num1//num2
else :
	print("invalid input!!!")
print("Result of the arithmetic operation is :",result)
