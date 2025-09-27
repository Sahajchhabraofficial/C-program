//wap to make a class for a complex number.
#include<iostream>
using namespace std;
class complex 
{
  int real;
  int imaginary;
public:  
    complex(){} 
    complex(int a,int b)
    {
        real=a;
        imaginary=b;
    }
    void display()
    {
        
        cout<<"complex number: "<<real<<" + "<<imaginary<<"i"<<endl;
        cout<<endl;

    }
    complex  operator+(complex object)
    {
        complex result;
        result.imaginary=imaginary+object.imaginary;
        result.real=real+object.real;
        return result;

    }
    complex operator-(complex object)
    {
        complex result;
        result.imaginary=imaginary-object.imaginary;
        result.real=real-object.real;
        return result;
    }
};
int main()
{
    complex c1(31,5),c2(54,3),c3,c4;
    c1.display();
    c2.display();
    c3=c1+c2;
    c4=c1-c2;
    c3.display();
    c4.display();
    return 0;
}