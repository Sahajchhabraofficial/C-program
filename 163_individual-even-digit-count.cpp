//Write a program that takes a number as input and counts how many even digits it contains.
#include<iostream>
using namespace std;
int main()
{
    int num,count=0,rem;
    cout<<"enter a number: ";
    cin>>num;
    while(num>0)
    {
        rem=num%10;
        if(rem%2==0)
        {
            count++;
        }
        num=num/10;
    }
    cout<<count;

    return 0;
}