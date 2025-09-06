#include<iostream>
using namespace std;
int main()
{
    //wap to take how many elements will present in the array from user.
    int ele,array[ele];
    cout<<"enter element number: ";
    cin>>ele;
    cout<<"enter array elements: ";
    for(int i=0;i<ele;i++)
    {
        cin>>array[i];
    }
    for(int i=0;i<ele;i++)
    {
        cout<<array[i]<<" ";
    }
    //wap to store only even elements in array.
    int arr[3];
    cout<<"enter array elements: ";
    for(int i=0;i<3;i++)
    {
        if(arr[i]%2==0)
        {
            cin>>arr[i];
        }
    }
    for(int i=0;i<5;i++)
    {
        cout<<arr[i]<<" ";
    }

    return 0;
}