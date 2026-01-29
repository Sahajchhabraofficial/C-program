#wap to reverse a four digit number given in input.
num=int(input("enter a number: "))
a=num%10
num=num//10
b=num%10
num=num//10
print("reverse number: ",b,a,num,sep="")