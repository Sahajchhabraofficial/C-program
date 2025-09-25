//wap to reverse a nuber without using strings.
#include<iostream>
using namespace std;
int main()
{
    int i,num,rem,rev=0;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        rem=num%10;
        cout<<rem;
        num=num/10;
    }

    return 0;
}