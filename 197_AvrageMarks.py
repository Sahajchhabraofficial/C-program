#Write a program to accept the marks of five subjects and calculate the average marks.
eng=int(input("enter english marks: "))
hin=int(input("enter marks of hindi: "))
math=int(input("enter marks of math: "))
sci=int(input("enter marks of science: "))
Sosci=int(input("enter marks of social science: "))
Avg=hin+eng+math+sci+Sosci/500
print("avrage marks of student is: ",Avg)