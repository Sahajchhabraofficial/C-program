#wap to swap values of any two variables without using a third variable.
a=5
b=6
print(f"Values before swapping a={a} and b={b}")
a=a+b
b=a-b
a=a-b
print(f"After swapping a={a} and b={b}")