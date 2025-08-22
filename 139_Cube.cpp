//Write a program to display number cube 1 to n (given number).
#include<iostream>
using namespace std;
int main()
{
    int i,num;
    i=1;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        cout<<i*i*i<<" ";
        i++;
    }

    return 0;
}