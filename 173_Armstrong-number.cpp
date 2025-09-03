//Wap to check given number is Armstrong or not if given number is three digit number. (153, 370, 371, 407).
#include<iostream>
using namespace std;
int main()
{
    int i=1,num,pow=3,sum=0,rem,arm;
    cout<<"enter a three digit number: ";
    cin>>num;//153
    arm=num;
    //while loop for finding sum of all numbers
    while(num>0)
    {
        rem=num%10;
        sum=sum+(rem*rem*rem);
        num=num/10;
    }
    //checking is a numener is equal to its sum or not.
    if(arm==sum)
    {
        cout<<"nunmber is armstrong";
    }
    else{
        cout<<"number is not arm strong";
    }
   
    return 0;
}