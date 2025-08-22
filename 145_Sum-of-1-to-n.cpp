//Write a program to display sum 1 to n (given number).
#include<iostream>
using namespace std;
int main()
{
    int i=1,sum=0,num;
    cout<<"enter a number : ";
    cin>>num;
    while(i<=num)
    {
        sum+=i;
        i++;
    }
    cout<<"sum= "<<sum;

    return 0;
}