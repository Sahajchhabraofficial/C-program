//Write a program to display factors of given number.
#include<iostream>
using namespace std;
int main()
{
    int i,num;
    cout<<"enter a number: ";
    cin>>num;
    cout<<"factors of number: ";
    for(i=1;i<=num;i++)
    {
        if(num%i==0)
        {
            cout<<i<<" ";
        }
    }

    return 0;
}