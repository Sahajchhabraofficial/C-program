#Write a program that inputs a student’s marks in three subjects (out of 100) and prints the percentage marks.
eng=int(input("enter english marks: "))
hin=int(input("enter hindi marks: "))
math=int(input("enter math marks: "))
sci=int(input("enter science marks: "))
SoSci=int(input("enter social science marks: "))
per=(hin+eng+math+sci+SoSci)/500*100
print("you got ",per,"% in this exam")
