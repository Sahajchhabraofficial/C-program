#wap to sort a list in aacending and decending order.
List=[34,81,42,65,24,55]
longed=[]
print("List in acendinng order: ")
shorted=sorted(List)
print(shorted)
print("List in decending order: ")
for i in range(len(shorted),0,-1):
    longed.append(shorted[i-1])
print(longed)