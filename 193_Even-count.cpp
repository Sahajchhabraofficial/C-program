//wap to print count of even elements of array.
#include<iostream>
using namespace std;
int main()
{
    int array[5],i,count=0;
    cout<<"enter array elements: ";
    for(i=0;i<5;i++)
    {
        cin>>array[i];
    }
    cout<<"number of even elements: ";
    for(i=0;i<5;i++)
    {
        if(array[i]%2==0)
        {
            count++;
        }
    }
    cout<<count;

    return 0;
}