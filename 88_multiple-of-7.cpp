//Write a program to display multiple of 7 between given range.
#include<iostream>
using namespace std;
int main()
{
    int start,end,i;
    cout<<"range starts with: ";
    cin>>start;
    cout<<"ends with: ";
    cin>>end;
    cout<<"multiple of 7 between given range: ";
    for(i=start;i<=end;i++)
    {
       if(i%7==0)
       {
          cout<<i<<" ";
       }
    }

    return 0;
}