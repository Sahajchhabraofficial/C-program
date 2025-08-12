//wap to check if a number is a armstrong number or not.
#include<iostream>
using namespace std;
int main()
{
    int i,sum,num,org,pow,len=0,rem;
    cout<<"enter a number: ";
    cin>>num;//456
    org=num;;
    while(num>0)
    {
        len++;
        num=num/10;
    }
    num=org;
    while(num>0)
    {
        rem=num%10;
        sum=1;
        for(i=1;i<=len;i++)
        {
            sum=sum*rem;
        }
        pow=pow+sum;
        num=num/10;
    }
    num=org;
    if(num==pow)
    {
        cout<<"it is a armstrong number"<<endl;
    }
    else{
        cout<<"it is not an armstrong number"<<endl;
    }

    return 0;
}