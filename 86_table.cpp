//Write a program to display table of given number.
#include<iostream>
using namespace std;
int main()
{
    int num,i;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=10;i++)
    {
        cout<<num<<" x "<<i<<" = "<<num*i<<endl;
    }

    return 0;
}