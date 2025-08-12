//wap to print sum of even number series 1 to n.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0;
    for(i=1;i<=20;i++)
    {
        if(i%2==0)
        {
            sum=sum+i;
        }
    }
    cout<<"sum of all even number: "<<sum;

    return 0;
}