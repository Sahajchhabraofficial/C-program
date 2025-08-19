//Write a program to check whether a number is a Strong Number or not.
#include<iostream>
using namespace std;
int main()
{
    int i,fact,sum=0,num,rem,org;
    cout<<"enter a number: ";
    cin>>num;
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
    num=org;
    if(num==sum)
    {
        cout<<"number is strong";
    }
    else{
        cout<<"number is not strong";
    }

    return 0;
}