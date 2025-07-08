//wap to show declearation of inheritence.
#include<iostream>
using namespace std;
class sample
{
public:
  void method1()
  {
    /*code*/
  }
  void method2()
  {
    /*code*/
  }
};
class sample2 :public sample
{
public:
    void method3()
    {
        /*code*/
    }
    void method4()
    {
        /*code*/
    }
};
int main()
{
    sample s1,s2,s3;
    sample2 ss1,ss2,ss3;
    s1.method1();
    s1.method2();
    ss1.method3();
    ss2.method4();
    ss3.method1();
    ss2.method1();

   return 0;
}