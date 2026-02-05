#wap to calculate grade of a student.
sub1=int(input("enter marks of hindi: "))
sub2=int(input("enter marks of english: "))
sub3=int(input("enter marks of maths: "))
per=((sub1+sub2+sub3)/300)*100
if int(per)<=33:
    print("Your grade is C")
elif int(per)>=60:
    print("Your grade is above B")
elif int(per)>=80:
    print("Your grade is above A")
else:
    print("BLAH!")
#this code is wrong bruah!