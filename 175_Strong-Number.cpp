//Write a program that takes a number as input and checks whether it is a Strong number or not.
#include <iostream>
using namespace std;
int main()
{
    int i=0,rem,sum=0,num,fact,org;
    cout<<"enter a number: ";
    cin>>num;//642
    org=num;
    while(num>0)
    {
        rem=num%10;
        fact=1;
        for(i=1;i<=rem;i++)
        {
            fact=fact*i;
        }
        sum=sum+fact;
        num=num/10;
    }
    if(org==sum)
    {
        cout<<"number is strong";
    }
    else{
        cout<<"number is not strong";
    }

    return 0;
}