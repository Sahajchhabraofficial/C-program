#Write a program to accept salary and credit score and determine loan eligibility
sal=int(input("enter your salary: "))
crdtscr=int(input("enter your credit score: "))
if sal>=50000 and crdtscr>=700:
    print("you are eligible for loan")
else:
    print("you are not eligible to loan")