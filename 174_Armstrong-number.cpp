//Write a program that takes a number as input and checks whether it is an Armstrong number or not.
#include<iostream>
using namespace std;
int main()
{
    int i=1,num,pow=0,sum=0,rem,arm,empty=0;
    cout<<"enter a three digit number: ";
    cin>>num;//153
    arm=num;
    //while loop for finding the length of number.
    while(num>0)
    {
        pow++;
        num=num/10;
    }
    num=arm;
    //while loop for finding sum of individual digits.
    while(num>0)
    {
        rem=num%10;
        sum=1;
        i=1;
        while(i<=pow)
        {
            sum=sum*rem;
            i++;
        }
        empty=empty+sum;
        num=num/10;
    }
    //checking if the number is equal to its sum or not.
    if(empty==arm)
    {
        cout<<"nunmber is armstrong";
    }
    else{
        cout<<"number is not arm strong";
    }
   
    return 0;
}