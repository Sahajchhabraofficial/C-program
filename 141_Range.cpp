//Write a program to display number between given range.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num;
    cout<<"enter Range: ";
    cin>>num;
    while(i<=num)
    {
        cout<<i<<" ";
        i++;
    }

    return 0;
}