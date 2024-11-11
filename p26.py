print("RECTANGLE"+"............")
l=int(input("Enter The Legth of The Rectangle  :"))
b=int(input("Enter The Breadth of The Rectangle :"))
area = lambda l, b: l * b
result= area(l,b) 
print("The Area of rectangle is..:",result)
perimeter = lambda l,b: 2*(l+b)
perimeter= perimeter(l,b)
print("The Perimeter of rectangle is...:",perimeter)
print("SQARE"+"............")
a=int(input("Enter the size of one side  :"))
sarea = lambda a: a*a
sarea = sarea(a)
print("The Area Of Square   :",sarea)
sperimeter = lambda a:4*a
sperimeter = sperimeter(a)
print("The Perimeter Of Square   :",sperimeter)
