//Write a program to find the sum of the series [1 +11 + 111 + 1111 + .. n ] terms.
#include<iostream>
using namespace std;
int main()
{
    int i,n,sum=0,num=1,b=10;
    cout<<"enter a number: ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
       cout<<num<<" ";
       sum=sum+num;
       num=num+b;
       b=b*10;
    }
    cout<<"sum of series =  "<<sum;

    return 0;
}