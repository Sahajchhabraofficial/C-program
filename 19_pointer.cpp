//pointer in cpp.
#include<iostream>
using namespace std;
int main()
{
   int *ptr,a;
   a=43;
   ptr=&a;
   cout<<"pointer address: "<<ptr<<endl;
   cout<<"a value: "<<a<<endl;
   cout<<"a value thorugh pointer: "<<*ptr<<endl;
   cout<<"a adress: "<<&a<<endl;

    return 0;
}
