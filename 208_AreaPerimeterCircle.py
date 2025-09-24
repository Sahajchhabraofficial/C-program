#Write a program to display a menu for calculating area of circle or perimeter of the circle.
print("======*Pick a choice*======")
print("1.Area of circle")
print("2.perimeter of circle")
status=input("->>")
if status=="Area":
    r=int(input("enter radius of circle: "))
    ar=22/7*r*r
    print("area of circle: ",int(ar),"cm^2")
else:
    r=int(input("enter radius of circle: "))
    peri=2*22/7*r*r
    print("perimeter of circle: ",int(peri),"cm^2")