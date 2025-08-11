//wap to check if a number is palindrome or not.
#include<iostream>
using namespace std;
int main()
{
    int i,rev=0,num,rem,org;
    cout<<"enter a number: ";//456
    cin>>num;
    org=num;
    for(i=0;num>0;i++)
    {
        rem=num%10;
        num=num/10;
        rev=rem*10+num;
    }
    cout<<"reverse number is: "<<rev;
    if(org==rev)
    {
        cout<<"number is palindrome"<<endl;
    }
    else{
        cout<<"number is not palindrome"<<endl;
    }

    return 0;
}