//Write a program to display factors of given number.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        if(num%i==0)
        {
            cout<<i<<" ";
        }
        i++;
    }

    return 0;
}