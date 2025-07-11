//alloting dynamic memory to array pointer.
#include <iostream>
using namespace std;
int main()
{
    int *ptr=new int [4];
    int *temp=ptr;
    int i;
    cout<<"enter array elements: ";
    for(i=0;i<4;i++)
    {
        cin>>*(ptr+i);
        ptr++;
    }
    ptr=temp;
    cout<<"array elements are: ";
    for(i=0;i<4;i++)
    {
        cout<<*(ptr+i)<<" ";
        ptr++;
    }
    ptr=temp;
    int sum=0;
    for(i=0;i<5;i++)
    {
        sum=sum+*(ptr+i);
        ptr++;
    }
    cout<<endl;
    cout<<"sum of the elements of array is : "<<sum;
    delete ptr;
    return 0;
}