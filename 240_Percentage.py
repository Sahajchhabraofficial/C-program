#Write a program that inputs a student’s marks in three subjects (out of 100) and prints the percentage marks.
marks1 = float(input("Enter marks for subject 1 (out of 100): "))
marks2 = float(input("Enter marks for subject 2 (out of 100): "))
marks3 = float(input("Enter marks for subject 3 (out of 100): "))
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100
print(f"Percentage marks: {percentage:.2f}%")