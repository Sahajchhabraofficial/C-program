//wap to print sum of odd number series.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0;
    for(i=1;i<=20;i++)
    {
        if(i%2!=0)
        {
            sum=sum+i;
        }
    }
    cout<<"sum of all odd numbers: "<<sum;

    return 0;
}