//HIRARICAL INHERTANCE.
#include<iostream>
using namespace std;
class student
{
    int rno;
    string name;
    float per;
public:
    void set_student(int r,float percentage,string nam)
    {
        name=nam;
        rno=r;
        per=percentage;
    }
    void display()
    {
        cout<<"STUDENT INFO:- "<<endl;
        cout<<"name: "<<name<<endl;
        cout<<"percentage: "<<per<<endl;
        cout<<"roll number: "<<endl;
    }
};
class commerce
{
   int accounts;
   int business_studies;
   int economics;
public:
    void set_marks(int eco,int acc,int bs)
    {
        economics=eco;
        accounts=acc;
        business_studies=bs;
    }
    void display_marks()
    {
        cout<<"MARKS INFO:- "<<endl;
        cout<<"economics: "<<economics<<endl;
        cout<<"accounts: "<<accounts<<endl;
        cout<<"business studies: "<<business_studies<<endl;
        cout<<"_________________________"<<endl;
    }
};
class science
{
   int physics;
   int math;
   int chemistry;
public:
    void set_marks(int chem,int phy,int math)
    {
        chemistry=chem;
        physics=phy;
        math=math;
    }
    void display_marks()
    {
        cout<<"MARKS INFO:- "<<endl;
        cout<<"chemistry: "<<chemistry<<endl;
        cout<<"physics: "<<physics<<endl;
        cout<<"math: "<<math<<endl;
        cout<<"_________________________"<<endl;
    }
};
class humanities
{
   int political_science;
   int math;
   int chemistry;
public:
    void set_marks(int chem,int phy,int math)
    {
        chemistry=chem;
        political_science=phy;
        math=math;
    }
    void display_marks()
    {
        cout<<"MARKS INFO:- "<<endl;
        cout<<"chemistry: "<<chemistry<<endl;
        cout<<"political_science: "<<political_science<<endl;
        cout<<"math: "<<math<<endl;
        cout<<"_________________________"<<endl;
    }
};
int main()
{
   science s1,s2;
   commerce c1,c2;
   humanities h1,h2;

    return 0;
}