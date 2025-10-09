//Write a function that takes an array and removes duplicate elements,
#include<iostream>
using namespace std;
int main()
{
    int arr[5]={1,5,2,3,2};
    int i,j;
    for(i=0;i<5;i++)
    {
        for(j=1;j<5;j++)
        {
            if(arr[i]==arr[j] && i!=j)
            {
                arr[i]=0;
            }
        }
    }
    cout<<"Array elements: ";
    for(i=0;i<5;i++)
    {
       cout<<arr[i]<<" "; 
    }

    return 0;
}