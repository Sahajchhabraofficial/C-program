//Print the series: 1! + 2! + 3! + … + n!.
#include<iostream>
using namespace std;
int main()
{
    int i,n;
    cout<<"enter a number: ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cout<<i<<"! + ";
    }

    return 0;
}