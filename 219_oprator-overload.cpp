//wap to overload operator + and add a complex number.
#include<iostream>
using namespace std;
class complex 
{
    int real;
    int img;
public:
    complex(){}
    complex(int a,int b)
    {
        real=a;
        img=b;
    }
    complex operator+(complex object)
    {
        complex result;
        result.img=img+object.img;
        result.real=real+object.real;
        return result;
    }
    void display()
    {
        cout<<"complex number: "<<real<<" + "<<img<<"i"<<endl;
    }
};
int main()
{
    complex num(5,3),num2(8,6),result;
    num.display();
    num2.display();
    result=num+num2;
    cout<<"=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-"<<endl;
    num.display();
    num2.display();

    return 0;
}