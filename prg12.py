def binarytodecimal(n,ex=1):
	if n==0:
		return 0
	else: 
		digit=n%10
		n=int(n/10)
		digit=digit*ex
		return digit+binarytodecimal(n,ex * 2)
n=int(input("enter any nymber:  "))
print("the decimal value is :",binarytodecimal(n))
