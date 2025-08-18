//Write a program to check how many number is divisible by 3,4 & 8 in between 21-121.
#include<iostream>
using namespace std;
int main()
{
    int i,three,eight,four,end=0;
    for(i=21;i<=121;i++)
    {
        if(i%3==0 || i%4==0 || i%8==0)
        {
            if(i%3==0 || i%4==0)
            {
               if(i%3==0)
               {
                  three++;
               }
               else{
                  four++;
               }
            }
            else{
                eight++;
            }
        }
    }

    cout<<"In this range there are divisible of: "<<endl;
    cout<<"Four: "<<four<<" times"<<endl;
    cout<<"Three: "<<three<<" times"<<endl;
    cout<<"Eight: "<<eight<<" times"<<endl;
    

    return 0;
}