#wap to check if a number is prime or not.
num=int(input("enter a number: "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("number is prime")
else:
    print("number is not prime")
