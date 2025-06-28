//Copy constructor.
#include <iostream>
using namespace std;
class employ
{
  int salary;
  string name;
public:
    employ(employ &emp)
    {
       name=emp.name;
       salary=emp.salary+5000;
    }
    void set_employ(int sal, string nam)
    {
      salary=sal;
      name=nam;
    }
    void get_employ()
    {
        cout<<"IMPLOY IDENTITY: "<<endl;
        cout<<"employ's name: "<<name<<endl;
        cout<<"employ's salary: "<<salary<<endl;
        cout<<"-------------------------"<<endl;
    }
};
int main()
{
   employ e1(e1), e2(e2);
    employ e3 = e2;                     
    e1.set_employ(25000,"arun");
    e1.set_employ(65000,"rajesh");
    e1.set_employ(10000,"mahi");
    e1.get_employ();
    e1.get_employ();
    e1.get_employ();
    return 0;
}