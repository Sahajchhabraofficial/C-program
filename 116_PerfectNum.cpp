//Write a program to find the 'Perfect' numbers within a given number of ranges (using nested loop).
#include<iostream>
using namespace std;
int main()
{
    int i,arr[5],fact,sum=0;
    cout<<"enter the range: ";
    for(i=1;i<=5;i++)
    {
        cin>>arr[i];
    }
    for(i=1;i<=arr[i];i++)
    {
        if(arr[i]%i==0)
        {
            sum=sum+i;
        }
        if(arr[i]==sum)
        {
           cout<<arr[i]<<" ";
        }
        
    }

    return 0;
}