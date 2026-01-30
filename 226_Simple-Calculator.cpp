//Create a program that simulates a simple calculator using switch case
#include<iostream>
using namespace std;
int Addition(int num1,int num2)
{
    int result;
    result=num1+num2;
    return result; 
}
int Subtraction(int num1,int num2)
{
    int result;
    result=num1-num2;
    return result;
}
int Multiplication(int num1,int num2)
{
    int result;
    result=num1*num2;
    return result;
}
float Devidation(int num1,int num2)
{
    float result;
    result=num1/num2;
    return result;
}
int main()
{
    int a,b;
    int choice;
    cout<<"======WELCOME TO CALCULATOR WORLD======"<<endl;
    cout<<"enter a number: ";
    cin>>a;
    cout<<"enter second number: ";
    cin>>b;
    cout<<"What would you like to do?"<<endl;
    cout<<"1.Addition"<<endl;
    cout<<"2.Subtraction"<<endl;
    cout<<"3.Multiplication"<<endl;
    cout<<"4.Devidation"<<endl;
    cout<<"-> ";
    cin>>choice;
    switch(choice)
    {
        case 1: cout<<Addition(a,b);break;
        case 2: cout<<Subtraction(a,b);break;
        case 3: cout<<Multiplication(a,b);break;
        case 4: cout<<Devidation(a,b);break;
        default: cout<<"you have entered above 4 number!"<<endl;
    }

    return 0;
}