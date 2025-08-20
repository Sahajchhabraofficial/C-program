//Calculate the result of following series:
//1+4+9+ 16. . . . . . . . . . . . . . . . . . . . . upto 10 terms.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0;
    for(i=1;i<=10;i++)
    {
        cout<<i*i<<" ";
        sum=sum+(i*i);
    }

    return 0;
}