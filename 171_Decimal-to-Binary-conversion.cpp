//Write a program to convert a binary number into a decimal number without using array, function and while loop.
#include<iostream>
using namespace std;
int main()
{
    int num,NUM,i=0,j,multA[6],multB[6],rem=0,binary=0;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1; ;++i)
    {
        if(num>0)
        {
            rem=num%2;
            cout<<binary<<" ";
            binary=binary*10+rem;
            num=num/10;
        }
        else{
           break;

        }
    }
    cout<<binary;

    return 0;
}