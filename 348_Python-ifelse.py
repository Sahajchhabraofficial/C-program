#Write a program to check whether a character is an special symbol or not.
cha=input("enter a character: ")
if ord(cha)>=32 and ord(cha)<=47 or ord(cha)>=58 and ord(cha)<=64 or ord(cha)>=91 and ord(cha)<=96 or ord(cha)>=123 and ord(cha)<=126:
    print("character is a special symbol")
else:
    print("character is not a special symbol")