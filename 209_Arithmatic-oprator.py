#Write a program that reads two numbers and an arithmetic operator and displays the computed result.
x=int(input("enter a number: "))
y=int(input("enter another number: "))
op=input("enter a arithmatic oprator: ")
if op=="plus":
    print("Addition: ",x+y)
elif op=="minus":
    print("Subtraction: ",x-y)
elif op=="multiply":
    print("Multiplication: ",x*y)
elif op=="devide":
    print("Devidation: ",x/y)
else:
    print("you entered wrong oprator!")
    