//Write a program to display number 1 to n (given number).
#include<iostream>
using namespace std;
int main()
{
    int i,num;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        cout<<i<<" ";
    }

    return 0;
}