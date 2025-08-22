//Write a program to display multiple of 7 between given range.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num;
    cout<<"enter a range: ";
    cin>>num;
    while(i<=num)
    {
        if(i%7==0)
        {
            cout<<i<<" ";
        }
        i++;
    }

    return 0;
}