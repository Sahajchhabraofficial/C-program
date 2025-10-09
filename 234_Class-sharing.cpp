//Simple inheritence
#include <iostream>
using namespace std;
class First
{
    int a;
    string b;
    char c;
    float d;
public:
    First(string name,int grade,char section,float percentage)
    {
        a=grade;
        b=name;
        c=section;
        d=percentage;
    }
    void display()
    {
        cout<<"STUDENT DETAILS:-"<<endl;
        cout<<"name: "<<b<<endl;
        cout<<"class: "<<a<<endl;
        cout<<"section: "<<c<<endl;
        cout<<"percentage: "<<d<<"%"<<endl;
    }
};
class Second:public First
{
    int e;
    string f;
public:
    Second(string name,int grade,char section,float percentage,int roll,string school):First(name,grade,section,percentage)
    {
        e=roll;
        f=school;
    }
    void show()
    {
        display();
        cout<<"roll no: "<<e<<endl;
        cout<<"school name: "<<f<<endl;
        cout<<"------------------"<<endl; 
    }
};
int main()
{
    Second std1("Balu",10,'H',78,10123,"GVR school");
    std1.show();

    return 0;
}