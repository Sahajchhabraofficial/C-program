//Write a program that takes a number as input and displays its digits in reverse order as a new number.
#include<iostream>
using namespace std;
int main()
{
    int num,rev,rem;
    cout<<"enter a number: ";
    cin>>num;
    cout<<"new number: ";
    while(num>0)
    {
        rem=num%10;
        cout<<rem;
        num=num/10;
    }

    return 0;
}