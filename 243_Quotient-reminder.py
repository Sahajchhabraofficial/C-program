#Write a program to read two numbers and prints their quotient and reminder.
num1 = int(input("Enter the first number (dividend): "))
num2 = int(input("Enter the second number (divisor): "))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient:", quotient)
print("Remainder:", remainder)