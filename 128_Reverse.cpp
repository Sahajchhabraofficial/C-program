//Print reverse of a given number.
#include<iostream>
using namespace std;
int main()
{
    int num,rem,rev=0;
    cout<<"enter a number: ";
    cin>>num;//2334
    while(num>0)
    {
        rem=num%10;
        cout<<rem;
        num=num/10;
    }

    return 0;
}