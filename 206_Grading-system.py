#Write a program to input a number and check whether it is positive, negative or zero.
hin=int(input("enter hindi nunmber: "))
eng=int(input("enter eng marks: "))
math=int(input("enter math marks: "))
science=int(input("enter science marks: "))
percentage=((hin+eng+math+science)/400)*100
print(percentage)
if percentage>=90:
    print("A Grade")
elif percentage>=75 and percentage<90:
    print("B Grade")
elif percentage>=60 and percentage<75:
    print("C Grade")
elif percentage<=60 and percentage<0:
    print("D Grade")