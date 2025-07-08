//SINGLE INHERITANCE EXAMPLE.
#include<iostream>
using namespace std;
class employ
{
  string name;
  int salary;
  int identity;
public:
  void set_employ(string nam,int sal, int id)
  {
    name=nam;
    salary=sal;
    identity=id;
  }
  void get_employ()
  {
    cout<<"EMPLOY INFO:- "<<endl;
    cout<<"name: "<<name<<endl;
    cout<<"id: "<<identity<<endl;
    cout<<"salary: "<<salary<<endl;
    cout<<"______________"<<endl;
  }
};
class programmer :public employ
{
  string language;
  string project;
public:
   void set_status(string lan,string pro)
   {
     language=lan;
     project=pro;
   }
   void display()
   {
    cout<<"PROJECT INFO:-"<<endl;
    cout<<"language: "<<language<<endl;
    cout<<"project name: "<<project<<endl;
    cout<<"_____________________________"<<endl;
   }
};
int main()
{
    programmer p1,p2;
    employ e1;
    p1.set_employ("satish",12500,106);
    p2.set_employ("gajendra",53000,104);
    p1.set_status("C++","apple watch");
    p2.set_status("Python","data handeling");
    p1.get_employ();
    p1.display();
    p2.get_employ();
    p2.display();


    return 0;
}