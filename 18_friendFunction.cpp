//friend function
#include<iostream>
using namespace std;
class base
{
  /*data membrs*/
public:
    void method1(/*args*/);
    void method2(/*args*/);
};
void method1(/*args*/)
{
   /*code*/
}
void method2(/*args*/)
{
   /*code*/
}
int main()
{
    base object;
    object.method1();
    object.method2();

    return 0;
}