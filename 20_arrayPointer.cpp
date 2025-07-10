//displaying an array though pointer.
#include <iostream>
using namespace std;
int main()
{
    int *ptr,arr[3]={12,73,32};
    int i;
    ptr=&arr[0];
    for(i=0;i<=3;i++)
    {
        cout<<*ptr<<" ";
        ptr++;
    }

    return 0;

}