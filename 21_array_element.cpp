//wap to display a array and print its sum of its elements.
#include<iostream>
using namespace std;
int main()
{
    int i,arr[4],*ptr,sum=0;
    cout<<"enter array elements: ";
    for(i=0;i<=4;i++)
    {
        cin>>arr[i];
    }
    cout<<"array elements are:"<<endl;
    for(i=0;i<=4;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    for(i=0;i<=4;i++)
    {
        sum=sum+arr[i];
    }
    cout<<"sum of the array elements are: "<<sum<<endl;
    

    return 0;
}