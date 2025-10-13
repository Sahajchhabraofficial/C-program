#wap to create a triangle of stars using nested loops.
for i in range(1,11):
    for j in range(1,i):
        if i==1 and j==1:
            print("          ",end="")
        elif i==2 and j==1:
            print("         ",end="")
        elif i==3 and j==1:
            print("        ",end="")
        elif i==4 and j==1:
            print("       ",end="")
        elif i==5 and j==1:
            print("      ",end="")
        elif i==6 and j==1:
            print("     ",end="")
        elif i==7 and j==1:
            print("    ",end="")
        elif i==8 and j==1:
            print("   ",end="")
        elif i==9 and j==1:
            print("  ",end="")
        elif i==10 and j==1:
            print(" ",end="")
        print("* ",end="")
    print()
for i in range(10, 0, -1):
    for j in range(10 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print() 