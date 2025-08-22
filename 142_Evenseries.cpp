//Write a program to display even number series.
#include<iostream>
using namespace std;
int main()
{
    int i=1,jio;
    cout<<"enter a number: ";
    cin>>jio;
    while(i<=jio)
    {
        if(i%2==0)
        {
            cout<<i<<" ";
        }
        i++;
    }

    return 0;
}