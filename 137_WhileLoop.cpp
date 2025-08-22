//Write a program to display number 1 to n (given number).
#include<iostream>
using namespace std;
int main()
{
    int i=1,num;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        cout<<i<<" ";
        i++;
    }

    return 0;
}