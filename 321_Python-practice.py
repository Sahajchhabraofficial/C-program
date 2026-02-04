#Write a program to accept roll no and marks of 3 subjects of a student, Calculate total of 3 subjects and average.
rollno=int(input("enter your rool no: "))
sub1=int(input("enter you marks of english: "))
sub2=int(input("enter marks of sicence: "))
sub3=int(input("enter marks of maths: "))
total=sub1+sub2+sub3
avg=total//3
print("Your avrage marks: ",int (avg))
print("your total marks: ",total)