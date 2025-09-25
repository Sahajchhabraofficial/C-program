//wap to check if a numebr is prime or not.
#include<iostream>
using namespace std;
int main()
{
    int count=0,i,num;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        if(num%i==0)
        {
            count++;
        }
    }
    if(count==2)
    {
        cout<<"number is prime";
    }
    else{
        cout<<"number is not prime";
    }

    return 0;
}