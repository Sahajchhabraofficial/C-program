#Write a program to accept the year and check if it is a leap year or not.
year=int(input("enter the year: "))
if year%4==0 and year>0 and year%100!=0:
    print("it is a leap year")
else: 
    print("it is not a leap year")