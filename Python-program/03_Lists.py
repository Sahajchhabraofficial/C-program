#wap to find the sum of all numbers ending with 4 in a list.
lst=[84,34,63,46,25,34,73,94,4]
add=0
for i in range(len(lst)):
    temp=lst[i]%10
    if temp==4:
        add=add+lst[i]
print("Sum of all numbers ending with 4 is:", add)