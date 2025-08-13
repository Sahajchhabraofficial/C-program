//Write a program to display average 1 to n ( given number).
#include<iostream>
using namespace std;
int main()
{
    int i,num,sum=0,avg;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        sum=sum+i;
    }
    avg=sum/num;
    cout<<"avarage of numbers 1 to "<<num<<": "<<avg;

    return 0;
}