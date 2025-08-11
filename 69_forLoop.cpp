//wap to check if a number is strong or not.
#include<iostream>
using namespace std;
int main()
{
    int num,i,fact,rem,org,sum=0;
    cout<<"enter a number: ";
    cin>>num;//145
    org=num;
    while(num>0)
    {
        fact=1;
        rem=num%10;
        for(i=1;i<=rem;i++)
        {
            fact=fact*i;
        }
        sum=sum+fact;
        num=num/10;
    }
    if(org==sum)
    {
        cout<<"number is strong"<<endl;
    }
    else{
        cout<<"number is not strong"<<endl;
    }

    return 0;
}