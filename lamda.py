a=int(input("enter the length of the rectangle"))
b=int(input("enter the breadth of the rectangle"))
area=lambda a,b:a*b
perimeter=lambda a,b:2*(a+b)
print("area of rectangle=",area(a,b))
print("perimeter of rectangle=",perimeter(a,b))
