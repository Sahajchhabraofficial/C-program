//Write a program takes a number as input and prints each digit of the number in reverse order,
// with each digit displayed on a separate line.
#include<iostream>
using namespace std;
int main()
{
    int num,rev,rem;
    cout<<"enter a number: ";
    cin>>num;
    while(num>0)
    {
        rem=num%10;
        cout<<rem<<endl;
        num=num/10;
    }

    return 0;
}