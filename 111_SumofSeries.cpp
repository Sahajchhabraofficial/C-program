//Write a program to display the sum of the series [ 9 + 99 + 999 + 9999 + .. n] terms.
#include<iostream>
using namespace std;
int main()
{
    int i,n,sum=0,b=90,num=9;
    cout<<"enter a number: ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cout<<num<<" ";
        sum=sum+num;
        num=num+b;
        b=b*10;
    }
    cout<<endl;
    cout<<"sum of series is: "<<sum;

    return 0;
}