//Write a program to find sum of all number between 1-25 and check sum is even or odd.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0;
    for(i=1;i<=25;i++)
    {
        sum=sum+i;
    }
    if(sum%2==0)
    {
        cout<<"sum is even";
    }
    else{
        cout<<"sum is odd";
    }

    return 0;
}