//wap to display student's details.
#include<iostream>
using namespace std;
class student
{
    int age;
    int marks;
    string name;
public:
    void set_student(int a,int mrk,string nam)
    {
        age=a;
        marks=mrk;
        name=nam;
    }
    void display_student()
    {
        cout<<"STUDENT DETAILS:-"<<endl;
        cout<<"name: "<<name<<endl;
        cout<<"age: "<<age<<endl;
        cout<<"marks: "<<marks<<endl;
        cout<<"================="<<endl;
    }
};
int main()
{
    student s1,s2;
    s1.set_student(16,79,"sahaj");
    s2.set_student(15,85,"raj");
    s1.display_student();
    s2.display_student();

    return 0;
}