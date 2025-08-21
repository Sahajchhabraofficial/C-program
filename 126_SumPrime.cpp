//Find the sum of all prime numbers between 1 and n.
#include<iostream>
using namespace std;
int main()
{
    int i,n,sum=0,count,j;
    cout<<"enter a number: ";
    cin>>n;
    for(i=1;i<=n;i++)
    {
        count=0;
        for(j=1;j<=i;j++)
        {
            if(i%j==0)
            {
                count++;
            }
        }
        if(count==2)
        {
            sum=sum+i;
        }
    }
    cout<<"sum of prime numbers present in 0 to "<<n<<" are "<<sum;

    return 0;
}