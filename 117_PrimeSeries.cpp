//Write a program to find the 'Prime' numbers within a given number of ranges (using nested loop).
#include<iostream>
using namespace std;
int main()
{
    int i,count,num;
    for(num=1;num<=100;num++)
    {
        count=0;
        for(i=1;i<=num;i++)
        {
            if(num%i==0)
            {
                count++;
            }
        }
        if(count==2)
        {
            cout<<num<<" ";
        }
    }

    return 0;
}