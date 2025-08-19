//Write a program to display the series [ 4,9,19,34,54..... n] terms.
#include<iostream>
using namespace std;
int main()
{
    int i,n,d=5,a=4,an,sum=0;
    cout<<"enter a number: ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cout<<a<<" ";
        sum=sum+a;
        a=a+d;
        d=d+5;
    }
    cout<<endl<<"series sum ="<<sum;
    return 0;
}