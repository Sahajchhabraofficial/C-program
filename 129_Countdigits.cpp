//Count digits in a given number.
#include<iostream>
using namespace std;
int main()
{
    int i,num,count=0;
    cout<<"enter a number: ";
    cin>>num;//678
    for(;0<num;)
    {
        count++;
        num=num/10;
    }
    cout<<count;

    return 0;
}