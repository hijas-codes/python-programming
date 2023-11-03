a=int(input("enter the number:  "))
sum=0
for i in range(1,a):
	if(a%i==0):
		sum=sum+i
if(sum==a):
	print("the number is perfect")
else:
	print("the number is  not perfect")
