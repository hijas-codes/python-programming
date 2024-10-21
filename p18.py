string = str(input("enter the string:"))
first_char=string[0]
bal_char=string[1::]
replaced=bal_char.replace(first_char,"$")
result=first_char+replaced
print(result)



