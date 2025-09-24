#Write a program to print whether a given character is an uppercase or a lowercase character or a digit or any other character.
char=input("enter a character: ")
if char>='A' and char<='Z':
    print("it is a capital letter")
elif char>='a' and char<='z':
    print("it is a small letter")
else:
    print("it is a special character")