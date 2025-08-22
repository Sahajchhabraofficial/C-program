//Write a program to display odd number series.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        if(i%2!=0)
        {
            cout<<i<<" ";
        }
        i++;
    }

    return 0;
}