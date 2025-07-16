//wap to represent pure virtual function.
#include<iostream>
using namespace std;
class base
{
public:
   int num1,num2;
    void set_data(int a,int b)
    {
        num1=a;
        num2=b;
    }
    virtual void  display() = 0;//pure virtual function
};
class derived:public base
{
public:
    void display()
    {
        cout<<"num1= "<<num1<<endl;
        cout<<"num2= "<<num2<<endl;
    } 
};
int main()
{
    derived obj;
    obj.set_data(52,66);
    obj.display();

    return 0;
}