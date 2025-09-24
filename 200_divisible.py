#Write a program that accepts two numbers and check if the first number is fully divisible by second number or not.
num1=int(input("enter a number: "))
num2=int(input("enter another number: "))
if num1%num2==0:
    print(f"{num2} is divisible by {num1}")
else:
    print(f"{num2} is not divisible by {num1}")