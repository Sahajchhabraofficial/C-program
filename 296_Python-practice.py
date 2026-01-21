#wap to find sum of individual digits with three digits.
a=252
for i in range(3):
    digit=a%10
    a=a//10
    digit_sum=digit if i==0 else digit_sum+digit
print(f"Sum of individual digits is: {digit_sum}")

