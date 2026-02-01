#wap to take 5 numbers from user and store them in a list.
List=[]
for i in range(1,6):
    element=int(input(f"Enter element {i}: "))
    List.append(element)
print(List)