//Write a program to that takes a number as input and calculates the sum of only its odd digits.
#include<iostream>
using namespace std;
int main()
{
    int num,sum=0,rem;
    cout<<"enter a number: ";
    cin>>num;
    while(num>0)
    {
        rem=num%10;
        if(rem%2!=0)
        {
            sum=sum+rem;
        }
        num=num/10;
    }
    cout<<"sum of odd digits: "<<sum;

    return 0;
}