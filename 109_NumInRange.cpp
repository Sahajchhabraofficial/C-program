//Wap to check given number in range of 1-20, if number in range than find sum of all number between this number to 20, otherwise print out of range.
#include<iostream>
using namespace std;
int main()
{
    int i,num,sum=0,end=2;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=20;i++)
    {
        if(num==i)
        {
           for(i=num;i<=20;i++)
           {
              sum=sum+i;
           }
        }
    }
    if(sum!=0)
    {
        cout<<"sum of range "<<num<<"-"<<"20 is: "<<sum<<endl;
    }
    else{
        cout<<"Number not in range"<<endl;
    }

    return 0;
}