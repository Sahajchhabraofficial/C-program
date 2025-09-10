#Write a program to find lowest among three integers.
num1=int(input("enter a number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num1<num2 and num1<num3:
    print(num1,"is smaller")
elif num2<num3:
    print(num2,"is smaller")
else:
    print(num3,"is smaller")
