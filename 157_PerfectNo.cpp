//Write a program to check given number is perfact or not.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num,sum=0;
    cout<<"enter a number: ";
    cin>>num;//6
    while(i<num)
    {
        if(num%i==0)
        {
            sum=sum+i;
        }
        i++;
    }
    if(num==sum)
    {
        cout<<"number is perfect";
    }
    else{
        cout<<"number is not perfect";
    }

    return 0;
}