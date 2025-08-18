//Write a program to check given number is perfact or not.
#include<iostream>
using namespace std;
int main()
{
    int i,num,sum=0,fact;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<num;i++)
    {
        if(num%i==0)
        {
            sum=sum+i;
        }
    }
    if(num==sum)
    {
        cout<<"Number is Perfect";
    }
    else{
        cout<<"Number is not Perfect";
    }

    return 0;
}