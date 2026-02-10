#Write a program to check given number is divisible by 3, 4 and 8 or not.
num=int(input("enter a number: "))
if num%3==0 and num%4==0 and num%8==0:
    print("number is divisible by 3,4 and 8")
else:
    print("number is not divisible by 3,4 and 8")