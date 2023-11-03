end = int(input("Enter the end of range: "))

for num in range( end + 1):
   if num > 1:
       for i in range(2, int(num**0.5) + 1):
           if (num % i) == 0:
               break
       else:
           print(num)
