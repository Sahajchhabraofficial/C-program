//HYBRID VIRTUAL BASE
#include<iostream>
using namespace std;
class super_class
{
  /* data members */
  public:
 void method()
 {
   cout<<"method 1 is called"<<endl;
 }
};
class side1 : virtual super_class
{

};
class side2 : virtual super_class
{

};
class sub_class:public side1,public side2
{
  
};
int main()
{
    sub_class sub;
    return 0;

}