//Write a program to check given number is prime or not.
#include<iostream>
using namespace std;
int main()
{
    int i=1,count=0,num;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        if(num%i==0)
        {
            count++;
        }
        i++;
    }
    if(count==2)
    {
        cout<<"number is prime ";
    }
    else{
        cout<<"number is not prime";
    }

    return 0;
}