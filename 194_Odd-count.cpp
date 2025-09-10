//wap to print count of odd element of array.
#include<iostream>
using namespace std;
int main()
{
    int array[5],i,count=0;
    cout<<"enter some array elements: ";
    for(i=0;i<5;i++)
    {
        cin>>array[i];
    }
    cout<<"number of odd elements present: ";
    for(i=0;i<5;i++)
    {
        if(array[i]!=0)
        {
            count++;
        }
    }
    cout<<count;

    return 0;
}