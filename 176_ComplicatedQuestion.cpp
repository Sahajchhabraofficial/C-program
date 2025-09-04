//Write a program that takes a number and repeatedly finds the sum of its digits until only a single digit remains (using nested while).
#include<iostream>
using namespace std;
int length(int Num)
{
    int count=0;
    while(Num>0)
    {
        count++;
        Num=Num/10;
    }
    
    return count;
}
int main()
{
    int i=1,num,rem,sum=0;
    cout<<"enter a number: ";
    cin>>num;//4566
    while(length(num)>1)
    {
        rem=num%10;
        sum=sum+rem;
        num=num/10;
    } 
    cout<<sum;
    
    return 0;
}