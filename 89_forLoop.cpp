//Write a program to display sum 1 to n ( given number).
#include<iostream>
using namespace std;
int main()
{
    int i,num,sum=0;
    cout<<"enter a num: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
       sum=sum+i;
    }
    cout<<"sum of numbers 1 to "<<num<<": "<<sum<<endl;

    return 0;
}