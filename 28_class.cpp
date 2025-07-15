#include<iostream>
using namespace std;
int main()
{
    int *ptr=new int [5];
    int i;
    cout<<"enter array elements: ";
    for(i=0;i<5;i++)
    {
        cin>>*(ptr+i);
    }
    cout<<"displaying array elements: ";
    for(i=0;i<5;i++)
    {
        cout<<*(ptr+i)<<" ";
    }
   delete ptr;
   return 0;
}