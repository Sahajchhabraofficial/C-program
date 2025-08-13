//Write a program to display number between given range.
#include<iostream>
using namespace std;
int main()
{
    int start,end,i;
    cout<<"range starts with: ";
    cin>>start;
    cout<<"end with: ";
    cin>>end;
    cout<<"Range: ";
    for(i=start;i<=end;i++)
    {
        cout<<i<<" ";
    }

    return 0;
}