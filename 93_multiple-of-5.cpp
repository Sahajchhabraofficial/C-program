//Write a program to display sum 1 to n ( given number) only multiple of 5 numbers sum.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0,num;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        if(i%5==0)
        {
            sum=sum+i;
        }
    }
    cout<<"sum of numbers 1 to "<<num<<"which are multiple of 5"<<": "<<sum;

    return 0;
}