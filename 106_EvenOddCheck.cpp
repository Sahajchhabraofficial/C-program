//Write a program to check how many numbers is even & odd between 77-165.
#include<iostream>
using namespace std;
int main()
{
    int i,even,odd;
    for(i=77;i<=165;i++)
    {
        if(i%2==0)
        {
            even++;
        }
        else{
            odd++;
        }
    }
    cout<<"there are "<<even<<" even numbers and "<<odd<<" odd numbers";

    return 0;
}