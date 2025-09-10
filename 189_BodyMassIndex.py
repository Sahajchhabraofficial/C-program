#Write a program that accepts weight in Kg and height in meters and calculate the BMI.
weight=int(input("enter weight in kg: "))
height=float(input("enter height in meters: "))
BMI=weight/height**2
print("your BMI is: ",BMI)
