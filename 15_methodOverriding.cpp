//Method overriding example
#include<iostream>
using namespace std;
class student
{
  string name;
  int rollnumber;
  float percentage;
public: 
    void set_student(int rno,float per,string nam)
    {
        rollnumber=rno;
        percentage=per;
        name=nam;
    }
    void display()
    {
       cout<<"STUDENT INFO:- "<<endl;
       cout<<"name :"<<name<<endl;
       cout<<"Roll Number: "<<rollnumber<<endl;
       cout<<"percentage: "<<percentage<<endl;
       cout<<"____________________"<<endl;
    }
};
class commerce:public student
{
   int economics;
   int accounts;
   int business_studies;
public:
     void set_marks(int acc,int eco,int bs)
     {
        business_studies=bs;
        economics=eco;
        accounts=acc;
     }
     void display()//overrided method
     {
        cout<<"COMMERCE STUDENT:-"<<endl;
        cout<<"economics: "<<economics<<endl;
        cout<<"business studies: "<<endl;
        cout<<"accounts: "<<accounts<<endl;
        cout<<"_____________________"<<endl;
     }
};
int main()
{
    commerce c1;
    c1.set_student(1120,61,"jayesh");
    c1.set_marks(65,53,55);
    c1.display();
    c1.display();
  

    return 0;

}