//wap to make a class for a complex numbers.
#include<iostream>
using namespace std;
class complex 
{
   int real;
   int imaginary;
public: 
   complex(int r,int img)
   {
      real=r;
      imaginary=img;
      cout<<"complex number: "<<real<<" + "<<imaginary<<"i";
   }

};

