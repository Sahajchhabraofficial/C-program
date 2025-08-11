//wap to print the sum of the numnbers ending with 3 in a array.
#include<iostream>
using namespace std;
int main()
{
    int arr[6]={35,43,86,63,65,93};
    int i,add=0;
    for(i=0;i<=6;i++)
    {
        if(arr[i]%10==3)
        {
           add=add+arr[i];
        }
    }
    cout<<"the sum of the numbres ending with 3 is: "<<add<<endl;

    return 0;
}