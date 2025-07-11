//how to point a object eith a pointer
#include<iostream>
using namespace  std;
class basic
{
  int memory;
public:
    void method(int mem)
    {
        memory=mem;
    }
    void method2()
    {
        cout<<"memory= "<<memory;
    }
};
int main()
{
    basic object;
    basic *ptr;
    ptr=&object;
    (*ptr).method(654);
    (*ptr).method2();


    return 0;
}
