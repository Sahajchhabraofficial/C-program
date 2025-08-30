//Write a to find the LCM (Least Common Multiple) of two numbers.
#include<iostream>
using namespace std;
int main()
{
    int num,NUM,i=0,j,multA[6],multB[6],rem=0,common=0;
    cout<<"enter first number: ";
    cin>>num;//6
    cout<<"enter second number: ";
    cin>>NUM;//4
    //while loop for finding multiples of first number.
    while(i<=5)
    {
        multA[i]=num*i;
        i++;
    }
    i=0;
    //while loop for finding multiples of second number.
    while(i<=5)
    {
        multB[i]=NUM*i;
        i++;
    }
    i=1;
    //while loop for finding common multiple between two numbers.
    i=0;
    while(i<=5)
    {
        for(j=0;j<=5;j++)
        {
            if(multA[i]==multB[j])
            {
                common=multA[i];
            }
        }
        i++;
    }
    cout<<endl;
    cout<<"LCM of the numbers is: "<<common;

    return 0;
}