//Write a program to swap two numbers using pointers.
#include<iostream>
using namespace std;
int main()
{
    int num1,num2;
    cout<<"enter first number: ";
    cin>>num1;
    cout<<"enter second number: ";
    cin>>num2;
    int *ptr1,*ptr2,temp;
    ptr1=&num1;
    ptr2=&num2;
    temp=*ptr1;
    *ptr1=*ptr2;
    *ptr2=temp;
    *ptr1=num1;
    *ptr2=num2;
    cout<<"first number: "<<num1<<endl;
    cout<<"second number: "<<num2<<endl;

    
    return 0;
}