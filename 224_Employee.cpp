//wap to create class for employees of a company and create a function in that which increases the salary by 10%.
#include<iostream>
using namespace std;
class Employee
{
public:
    int id;
    string name;
    float salary;
public:
    friend void increment();
    void set_employe(int id,string name,int salary)
    {
        this->id=id;
        this->name=name;
        this->salary=salary;
    }
    void display()
    {
        cout<<"EMPLOYEE DETAILS:-"<<endl;
        cout<<"name: "<<name<<endl;
        cout<<"id: "<<id<<endl;
        cout<<"salary: "<<salary<<endl;
        cout<<"=-=-=-=-=-=-=-=-=-=-"<<endl;
    }
};
void increment(Employee obj)
{
    obj.salary=obj.salary*1.10;
}
int main()
{
    Employee rajesh,mohit,jason;
    rajesh.set_employe(1501,"Rajesh Kumar",12000);
    mohit.set_employe(1502,"mohit chandak",26000);
    jason.set_employe(1503,"jason smith",50000);
    rajesh.display();
    mohit.display();
    increment(jason);
    jason.display();

    return 0;
}