#wap to find sum of any three digit number.
num=int(input("enter any number: "))
a=num%10
num=num//10
b=num%10
num=num//10
print("sum of individual number: ",(a+b+num))