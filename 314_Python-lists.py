#wap to remove duplicate elements from a list.
#WRONG WAY!!
"""  List=[54,32,92,32,72,10]
     print("List before removing",List)
     for i in range(len(List)):
         ele=List[i]
         for List[i] in List:
             if List[i]==ele:
                 List.pop(i)
     print("List after removing",List)"""

#CORRECT WAY!!
List=[54,32,92,32,72,10]
print("List before removing",List)
new_List=[]
for i in List:
    if i not in new_List:
        new_List.append(i)
print("List after removing",new_List)
