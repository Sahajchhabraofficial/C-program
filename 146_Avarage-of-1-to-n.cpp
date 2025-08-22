//Write a program to display average 1 to n ( given number).
#include<iostream>
using namespace std;
int main()
{
    int i=1,avg=0,num,sum=0;
    cout<<"enter a number: ";
    cin>>num;
    while(i<=num)
    {
        sum=sum+i;
        i++;
    }
    avg=sum/num;
    cout<<"avg= "<<avg;

    return 0;
}