//wap to print elements of array in reverse order.
#include<iostream>
using namespace std;
int main()
{
    int arr[4],i;
    cout<<"enter some numbers: ";
    for(i=0;i<4;i++)
    {
        cin>>arr[i];
    }
    cout<<"reversed array: ";
    for(i=3;i>=0;i--)
    {
        cout<<arr[i]<<" ";
    }

    return 0;
}