//wap to print only negative elements of array.
#include<iostream>
using namespace std;
int main()
{
    int integers[5],i;
    cout<<"enter some integers: ";
    for(i=0;i<5;i++)
    {
        cin>>integers[i];
    }
    cout<<"negative elements of array: ";
    for(i=0;i<5;i++)
    {
        if(integers[i]<0)
        {
            cout<<integers[i]<<" ";
        }
    }

    return 0;
}