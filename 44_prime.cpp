//wap to check if a number is prime or not.
#include<iostream>
using namespace std;
int Prime(int pri)
{
    int i,count;
    for(i=1;i<=pri;i++)
    {
       if(pri%i==0)
       {
          count++;
       }
    }
    if(count<=2)
    {
        return true;
    }
    else{
        return false;
    }
}
int main()
{
    int num;
    cout<<"enter a number: ";
    cin>>num;
    if(Prime(num)==true)
    {
        cout<<"this is a prime number"<<endl;
    }
    else{
        cout<<"number is not prime"<<endl;
    }

    return 0;
}