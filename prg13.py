def fib(a):
	c=0
	if(a==0 or a==1):
		return a
	else:
		c=fib(a-1)+(a+2)
		return c
d=int(input("enter any number:"))
for i in range(0,d):
	print(fib(i))
