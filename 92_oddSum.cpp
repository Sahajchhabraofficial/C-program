//Write a program to display sum 1 to n ( given number) only odd numbers sum.
#include<iostream>
using namespace std;
int main()
{
    int i,num,sum=0;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        if(i%2!=0)
        {
            sum=sum+i;
        }
    }
    cout<<"sum of odd numbers 1 to "<<num<<": "<<sum<<endl;

    return 0;
}