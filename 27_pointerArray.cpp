//calling a method odf a class through a pointer
#include <iostream>
using namespace std;
class student
{ 
   string name;
   int rollnumber;
   float percentage;
public:
    void set_student(string nam, int rno, float per)
    {
        name=nam;
        rollnumber=rno;
        percentage=per;
    }
    void display()
    {
        cout<<endl;
        cout<<"STUDENT INFO:- "<<endl;
        cout<<"name: "<<name<<endl;
        cout<<"percentage: "<<percentage<<endl;
        cout<<"roll number: "<<endl;
        cout<<"___________________"<<endl;
    }
}; 
int main()
{
    student *ptr=new student[2],*temp;
    temp=ptr;
    string name;
    int rollnumber;
    float percentage;
    int i;
    for(i=0;i<2;i++)
    {
        cout<<"enter name: ";
        cin>>name;
        cout<<"entre roll number: ";
        cin>>rollnumber;
        cout<<"enter percentage: ";
        cin>>percentage;
        ptr++;
        ptr->set_student(name,rollnumber,percentage);
    }
    ptr=temp;
    cout<<endl;
    cout<<"=-=-=-=-=-=-=-=-=-=-=-=-=-="<<endl;
    for(i=0;i<2;i++)
    {
        ptr->display();
        ptr++;
    }

    delete ptr;
    return 0;
}
