//trying to generate random value using garbage value.
#include<iostream>
using namespace std;
int main()
{
    int var[3],sum=0;
    start:
    for(int i=0;i<=3;i++)
    {
        sum=sum+var[i];
    }
    if(sum==0)
    {
        goto start;
    }
    else{
        cout<<"your random value: "<<sum;
    }

    return 0;
}
//FAILED!!...