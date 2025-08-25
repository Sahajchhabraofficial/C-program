//Write a program to takes a number as input and calculates the sum of its individual digits.
#include<iostream>
using namespace std;
int main()
{
    int i=1,sum=0,rev=0,rem,num;
    cout<<"enter a number: ";
    cin>>num;
    while(num>0)
    {
        rem=num%10;
        sum=sum+rem;
        num=num/10;
    }
    cout<<"sum of individual digits: "<<sum;

    return 0;
}