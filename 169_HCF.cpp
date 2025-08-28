//Write a to find the HCF of two numbers.
#include<iostream>
using namespace std;
int main()
{
    int factA=0,factB=0,a,b,i=1,j=1,count=0,rem,vem,sum=0;
    cout<<"enter first number: ";
    cin>>a;//60
    cout<<"enter second number: ";
    cin>>b;//75
    //while loop for finding factors of prime number.
    while(i<=a)
    {
        if(a%i==0)
        {
            while(i<=j)
            {
                if(i%j==0)
                {
                    count++;
                }
                j++;
            }
            if(count==2)
            {
                factA=factA*10+i;
            }
        }
        i++;
    }
    i=1,count=0,j=1;
    //while loop for finding factors of second number.
    while(i<=b)
    {
        if(b%i==0)
        {
            while(i<=j)
            {
                if(i%j==0)
                {
                    count++;
                }
                j++;
            }
            if(count==2)
            {
                factB=factB*10+i;
            }
        }
        i++;
    }
    j=1,count=0;
    cout<<factA<<" "<<factB;
    //while loop for finding heighest common factors.
    /*while(factA>0)
    {
        rem=factA%10;
        
        factA=factA/10;
    }*/

    return 0;
}