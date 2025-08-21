//Calculate the result of following series:
//1+3+7+15 . . . . . . . . . . . . . . . . . . . . . upto 10 terms.
#include<iostream>
using namespace std;
int main()
{
    int i,ser=1,inc=2,sum=0;
    for(i=1;i<=10;i++)
    {
        cout<<ser<<" ";
        sum=sum+ser;
        ser=ser+inc;
        inc=inc*2;
    }
    cout<<endl;
    cout<<"result of the series: "<<sum;

    return 0;
}