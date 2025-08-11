//wap to check if a numeber is prime or not.
#include<iostream>
using namespace std;
int main()
{ 
    int i,num,count;
    cout<<"enter a number: ";
    cin>>num;//15
    for(i=1;i<=num;i++)
    {
        if(num%i==0)
        {
            count++;
        }
    }
    cout<<count;
    if((count-1)<=2)
    {
        cout<<"number is prime"<<endl;
    }
    else{
        cout<<"number is not prime"<<endl;
    }

    return 0;
}