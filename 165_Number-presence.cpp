//Write a program that takes a number and a single digit as input, and checks whether the digit exists in the given number or not.
#include<iostream>
using namespace std;
int main()
{
    int i,num,dig,rem,status=0;
    cout<<"enter a number: ";
    cin>>num;
    cout<<"enter the digit: ";
    cin>>dig;
    while(num>0)
    {
        rem=num%10;
        if(rem==dig)
        {
            status=5;
            break;
        }
        num=num/10;
    }
    if(status==5)
    {
        cout<<"Number Found!";
    }
    else{
        cout<<"Number not Found!";
    }

    return 0;
}