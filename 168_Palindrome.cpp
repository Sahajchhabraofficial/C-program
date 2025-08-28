//Write a program that takes a number as input and checks whether it is a palindrome or not.
#include<iostream>
using namespace std;
int main()
{
    int num,rem,org,rev=0;
    cout<<"Enter a number: ";
    cin>>num;//7557
    org=num;
    while(num>0)
    {
        rem=num%10;
        rev=rev*10+rem;
        num=num/10;
    }
    if(org==rev)
    {
        cout<<"number is palindrome";
    }
    else{
        cout<<"number is not palindrome";
    }

    return 0;
}