#wap to find sum of individual digits of a four digit number.
num=int(input("enter a number: "))#3831
a=num%10
num=num//10

b=num%10
num=num//10

c=num%10
num=num//10

print("sum of invdividual digits: ",(a+b+c+num))