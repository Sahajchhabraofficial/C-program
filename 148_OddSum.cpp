//Write a program to display sum 1 to n ( given number) only odd numbers sum.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num,sum=0;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        if(i%2==0)
        {
            sum=sum+i;
        }
        i++;
    }
    cout<<"sum of odd numbers: "<<sum;

    return 0;
}