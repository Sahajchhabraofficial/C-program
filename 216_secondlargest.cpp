//wap to print largest element in the array.
#include<iostream>
using namespace std;
int main()
{
    int arr[5]={46,62,65,87,24},lar=arr[0];
    for(int i=0;i<5;i++)
    {
        if(arr[i]>arr[i+1])
        {
            lar=arr[i];
        }
    }
    cout<<lar;

    return 0;
}