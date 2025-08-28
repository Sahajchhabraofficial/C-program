//Write a program that takes a number and a single digit as input, and counts how many times the digit appears in the given number.
#include<iostream>
using namespace std;
int main()
{
    int num,dig,count=0,rem;
    cout<<"enter a number: ";
    cin>>num;
    cout<<"enter a digit: ";
    cin>>dig;
    while(num>0)
    {
        rem=num%10;
        if(rem==dig)
        {
            count++;
        }
        num=num/10;
    }
    cout<<count;

    return 0;
}