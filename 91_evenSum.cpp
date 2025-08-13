//Write a program to display sum 1 to n ( given number) only even numbers sum.
#include<iostream>
using namespace std;
int main()
{
    int sum=0,num,i;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        if(i%2==0)
        {
            sum-sum+i;
        }
    }
    cout<<"sum of even numbers 1 to "<<num<<": "<<sum;

    return 0;
}