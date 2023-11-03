l=100
n=int(input("enter any number"))
c=0
for num in range(1,l):
	if c<n:
		if num>1:
			for d in range(2,num):
				if(num%d)==0:
					break
			else:
				print(num)
				c=c+1
