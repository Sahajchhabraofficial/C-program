//Calculate power of a number without using pow().
#include<iostream>
using namespace std;
int main()
{
    int i,num,pow,ans=1;
    cout<<"enter a number: ";
    cin>>num;//2
    cout<<"enter another num: ";
    cin>>pow;//3
    for(i=1;i<=pow;i++)
    {
       ans=ans*num;
    }
    cout<<num<<" to the power "<<pow<<": "<<ans;

    return 0;
}