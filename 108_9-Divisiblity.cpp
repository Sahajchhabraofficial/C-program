//Write a program to find the number and sum of all integers between 100 and 200 which are divisible by 9.
#include<iostream>
using namespace std;
int main()
{
    int i,sum;
    for(i=100;i<=200;i++)
    {
        if(i%9==0)
        {
            sum=sum+i;
        }
    }
    cout<<"sum of numbers devisible by 9 between 100 and 200 are: "<<sum<<endl;

    return 0;
}
