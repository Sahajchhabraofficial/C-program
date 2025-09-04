//Write a program to find and display the first and last digit of a given number.
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
    int num,rem,first,last,sum=0;
    cout<<"enter a number: ";
    cin>>num;//5127
    last=num%10;
    while(length(num)>1)
    {
        rem=num%10;
        sum=sum+rem;
        num=num/10;
    } 
    first=num;
    cout<<"first num: "<<first<<endl;
    cout<<"last num: "<<last<<endl;

    return 0;
}