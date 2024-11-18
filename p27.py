class Rectangle():
	def __init__(self,l,w):
		self.length = l
		self.width  = w
	def area(self):
		return self.length*self.width
	def peri(self):
		return 2*(self.length+self.width)
a=int(input("Enter the length of the rectangle  :"))
b=int(input("Enter the width of the rectangle :"))
obj=Rectangle(a,b)
print("Area =",obj.area())
print("Perimeter",obj.peri())


