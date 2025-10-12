#Write a program to compute area of square and triangle.
side = int(input("Enter side length of square: "))
area_square = side * side
base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
area_triangle = 0.5 * base * height
print("Area of square is:", area_square)
print("Area of triangle is:", area_triangle)