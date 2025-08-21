//Write a program to display the n terms of a harmonic series and their sum. 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=0,inc=1,num,ser=1;
    cout<<"enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        cout<<ser/i<<" ";
        sum=sum+ser;
    }
    cout<<endl;
    cout<<"sum of harmonic series: "<<sum;

    return 0;
}