//Calculate power of a number without using pow().
#include<iostream>
using namespace std;
int main()
{
    int i=1,num,pow,ans=1;
    cout<<"enter a number: ";
    cin>>num;//3
    cout<<"to the power: ";
    cin>>pow;//2
    while(i<=pow)
    {
        ans=ans*num;
        i++;
    }
    cout<<ans<<" ";
    
    return 0;
}