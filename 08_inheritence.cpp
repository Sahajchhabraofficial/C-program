//wap to make a class for class 11th students.
#include<iostream>
using namespace std;
class student
{
  string name;
  char section;
  int roll_number;
  float percentage;
public: 
     void set_student(string nam,char sec,int rno,float per)
     {
        name=nam;
        section=sec;
        roll_number=rno;
        percentage=per;
     }
     void report_card()
     {
        cout<<"STUDENT'S REPORT CARD:-"<<endl;
        cout<<"student's name: "<<name<<endl;
        cout<<"student's section: "<<section<<endl;
        cout<<"student's roll number: "<<roll_number<<endl;
        cout<<"student's percentage: "<<percentage<<endl;
        cout<<"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"<<endl;
     }
};
class commerce
{
    int economics;
    int accounts;
    int business_studies;
public:
    void set_marks(int eco, int acc,int bs)
    {
       economics=eco;
       accounts=acc;
       business_studies=bs;
    }
    void display_marks()
    {
        cout<<"MARKS INFO:-"<<endl;
        cout<<"economics marks: "<<economics<<endl;
        cout<<"accounts marks: "<<accounts<<endl;
        cout<<"business studies marks: "<<business_studies<<endl;
        cout<<"___________________________________";
    }
};
class science
{
    int physics;
    int chemistry;
    int math;
public:
    void set_marks(int phy, int chem,int math)
    {
       physics=phy;
       chemistry=chem;
       math=math;
    }
    void display_marks()
    {
        cout<<"MARKS INFO:-"<<endl;
        cout<<"physics marks: "<<physics<<endl;
        cout<<"chemistry marks: "<<chemistry<<endl;
        cout<<"Math studies marks: "<<math<<endl;
        cout<<"___________________________________";
    }
};
class humanitis
{
    int political_science;
    int history;
    int english;
public:
    void set_marks(int ps, int his,int eng)
    {
       political_science=ps;
       history=his;
       english=eng;
    }
    void display_marks()
    {
        cout<<"MARKS INFO:-"<<endl;
        cout<<"physics marks: "<<political_science<<endl;
        cout<<"chemistry marks: "<<history<<endl;
        cout<<"Math studies marks: "<<english<<endl;
        cout<<"___________________________________";
    }
};