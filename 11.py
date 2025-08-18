#Write a program that inputs a student’s marks in three subjects (out of 100) and prints the percentage marks.
hin=int(input("enter the marks of hindi: "))
math=int(input("enter the marks of math: "))
eng=int(input("enter the marks of ehglish: "))
per=(hin+eng+math/300)*100
print("your percentage is :",per)
