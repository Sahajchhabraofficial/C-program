//Write a program to display table of given number.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=10)
    {
        cout<<i<<" x "<<num<<" = "<<num*i<<endl;
        i++;
    }

    return 0;
}