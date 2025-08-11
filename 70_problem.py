#wap to print sum of all the numbers ending with 3 in a list.
list1=[54,65,98,33,73,13]
add=0
for i in range(len(list1)):
        if(list1[i]%10 ==3):
            add=add+list1[i]

print("the sum of the numbers ending with 3 are: ",add)
    
