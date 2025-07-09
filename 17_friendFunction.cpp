//friend functiomn
#include<iostream>
using namespace std;
class employ
{
   int identity;
   float salary;
public:
    void set_employ(int a,float b);
    void get_employ();
};
void employ::set_employ(int sal,float id)
{
   salary=sal;
   identity=id;
}
void employ::get_employ()
{
    cout<<"EMPLOY INFO:- "<<endl;
    cout<<"salary: "<<salary<<endl;
    cout<<"identity: "<<identity<<endl;
    cout<<"_________________"<<endl;
}
int main()
{
    employ e1,e2;
    e1.set_employ(655,12000.85);
    e2.set_employ(354,2103.36);
    e1.get_employ();
    e2.get_employ();
    
    return 0;
}