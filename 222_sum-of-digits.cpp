//Find the sum of digits of a number using a loop.
#include<iostream>
using namespace std;
int main()
{
    int num=6543,i,sum=0,rem;
    for(i=0;i<=4;i++)
    {
        rem=num%10;
        sum=sum+rem;
        num=num/10;
    }
    cout<<"sum of number is: "<<sum;

    return 0;
}