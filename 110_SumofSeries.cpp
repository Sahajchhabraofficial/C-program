//Write a program to find the sum of the series [1 +11 + 111 + 1111 + .. n ] terms.
#include<iostream>
using namespace std;
int main()
{
    int i,n,sum=1;
    cout<<"enter a number: ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
        if(i==1)
        {
            continue;
        }
        else{
            sum=sum+sum*10+1;
        }
    }
    cout<<"sum of series from 1 to "<<n<<" is: "<<sum;

    return 0;
}