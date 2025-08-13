//Write a program to display factors count of given number.
#include<iostream>
using namespace std;
int main()
{
    int i,count,num;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<num;i++)
    {
        if(num%i==0)
        {
            count++;
        }
    }
    cout<<num<<" has "<<count<<" factors";

    return 0;
}