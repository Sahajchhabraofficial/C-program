//wap to take array element from user and display it by adding 5 to it.
#include<iostream>
using namespace std;
int main()
{
    int arr[3],i;
    cout<<"enter array elements: ";
    for(i=0;i<3;i++)
    {
        cin>>arr[i];
    }
    cout<<"array element by adding 5 to each: ";
    for(i=0;i<3;i++)
    {
        cout<<arr[i]+5<<" ";
    }

    return 0;
}