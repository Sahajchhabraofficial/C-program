//Calculate the result of following series:
//1+3+5+7 . . . . . . . . . . . . . . . . . . . . . upto 10 terms.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0,ser=1;
    for(i=1;i<=10;i++)
    {
        cout<<ser<<" ";
        sum=sum+ser;
        ser=ser+2;
    }

    return 0;
}