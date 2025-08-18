//Write a program to display the sum of the series [ 9 + 99 + 999 + 9999 + .. n] terms.
#include<iostream>
using namespace std;
int main()
{
    int i,n,sum=9;
    cout<<"enter a number: ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
        if(i==1)
        {
            continue;
        }
        else{
            sum=sum+sum*10+9;
        }
        // cout<<sum<<endl;
    }
    cout<<"sum of series from 1 to "<<n<<" is: "<<sum;

    return 0;
}