#Write a program to input a number and print its square if it is odd, otherwise print its square root.
num=int(input("enter a number: "))#16
if num%2!=0:
    print("square: ",num**2)
else:
    print("square root: ",int((num**1/2)/2))