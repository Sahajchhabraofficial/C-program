
#include<iostream>
using namespace std;
class father
{
public:
   int num1;
public:
    father(int a)
    {
       num1=a;
    }
    virtual void display()
    {
       cout<<"num1= "<<num1<<endl;
    }
};
class child: public father
{
    int num2;
public:
    child(int a,int b):father(a)
    {
        num1=a;
        num2=b;
    }
    virtual void display()
    {
        cout<<"num2= "<<num2<<endl;
        cout<<"num1= "<<num1<<endl;
    }
};
int main()
{
    father *ptr=new father(345);
    ptr->display();
    cout<<"________________________"<<endl;
    ptr=new child(78,652);
    ptr->display();

    return 0;
}