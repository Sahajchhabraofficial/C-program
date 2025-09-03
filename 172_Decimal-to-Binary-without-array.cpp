//Write a program to convert a decimal number into binary without using an array.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num,mult=0,Rem,div,rem;
    cout<<"enter a number: ";
    cin>>num;//45
    div=num;
    
    while(div<=1)
    {
        Rem=div%2;
        div=num/2;
    }
    cout<<Rem;
    cout<<endl;
    while(num>0)
    {
        rem=Rem%10;
        cout<<rem;
        num=num/10;
    }

    return 0;
}