#wap to find the mean of gieen numbers in a list.
lst=[1,2,3,4,5]
add=0
for j in range(5):
    lst[j]=int(input("Enter the number: "))
    add=add+lst[j]
mean=add/5
print("Mean of the numbers is:", mean)