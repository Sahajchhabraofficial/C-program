#Write a program to check whether a character is an alphabet or not.
alpha=input("enter a character: : ")
if ord(alpha)>=65 and ord(alpha)<=90 or ord(alpha)>=97 and ord(alpha)<=122:
    print("character is an alphabet")
else:
    print("character is not a alphabet")