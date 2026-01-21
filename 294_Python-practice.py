#wap to swap values of any three numbers without using a fourth variable.
a=5 
b=6
c=7
print(f"Values before swapping a={a}, b={b} and c={c}")
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print(f"After swapping a={a}, b={b} and c={c}")