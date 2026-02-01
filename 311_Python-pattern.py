#wap to make a ABCD wala pattern with python.
Letters=[" ","A","B","C","D"]
i=1
for i in range(len(Letters)):#rows
    for j in range(i):#column
        print(Letters[i],end="")
    print()