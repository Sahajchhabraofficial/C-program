#Write a program to check whether a character is an digit or not
cha=input("enter a character: ")
if ord(cha)>=48 and ord(cha)<=57:
    print("character is a digit")
else:
    print("character is not a digit")