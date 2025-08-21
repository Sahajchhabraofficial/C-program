//Calculate the result of following series:
//2+4+6+8 . . . . . . . . . . . . . . . . . . . . . upto 10 terms.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0,ser=2;
    for(i=1;i<=10;i++)
    {
        cout<<ser<<" ";
        sum=sum+ser;
        ser=ser+2;
    }
    cout<<endl;
    cout<<"result of the series: "<<sum;

    return 0;
}