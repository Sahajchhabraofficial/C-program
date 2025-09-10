//wap to print only positive elements of array.
#include<iostream>
using namespace std;
int main()
{
    int integers[5];
    cout<<"enter some integers: ";
    for(int i=0;i<5;i++)
    {
        cin>>integers[i];
    }
    cout<<"positive elements of array: ";
    for(int i=0;i<5;i++)
    {
        if(integers[i]>0)
        {
            cout<<integers[i]<<" ";
        }
    }

    return 0;
}