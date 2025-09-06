#include<iostream>
using namespace std;
int main()
{
    //wap to display an array through for loop.
    int array[5]={465,665,762,297,378};
    for(int i=0;i<5;i++)
    {
        cout<<array[i]<<" ";
    }
    //wap to do sum of all elements in the array.
    int i,sum=0;
    for(i=0;i<5;i++)
    {
        sum=sum+array[i];
    }
    cout<<endl;
    cout<<sum;
    cout<<endl;
    //wap to take user input of array elements.
    int arr[4];
    cout<<"enter array elements: ";
    for(i=0;i<4;i++)
    {
        cin>>arr[i];
    }
    for(i=0;i<5;i++)
    {
        cout<<arr[i]<<" ";
    }

    return 0;
} 