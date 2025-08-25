//Write a program to display factors count of given number.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num,count=0;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        if(num%i==0)
        {
            count++;
        }
        i++;
    }
    cout<<num<<" has "<<count<<" factors ";

    return 0;
}