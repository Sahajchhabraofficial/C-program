#Write a program to accept two numbers and check if the first is a multiple of the second.
num=int(input("enter a number: "))
a=int(input("enter a nother number: "))
if num%a==0:
    print("number is multiple of ",a)
else:
    print("number is not a multple of ",a)
    