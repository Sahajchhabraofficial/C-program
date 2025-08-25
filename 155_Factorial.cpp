//Write a program to display factorial of given number.
#include<iostream>
using namespace std;
int main()
{
    int i=1,fact=1,num;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        fact=fact*i;
        i++;
    }
    cout<<"factorial= "<<fact;

    return 0;
}