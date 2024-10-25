n=int(input("enter the limit:   "))
names=[]
for i in range(n):
	name=input(f"enter name{i+1}")
	names.append(name)
	names.sort()
print(f"sorted list:  \n {names}")
