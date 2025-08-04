//wap to make a class which shows its information
#include<iostream>
using namespace std;
class Student
{
   string name;
   char grade;
public: 
   Student(string name,char grade)
   {
      this->grade=grade;
      this->name=name;
   }
   void display()
   {
      cout<<endl;
      cout<<"student info:-"<<endl;
      cout<<"student name: "<<name<<endl;
      cout<<"student's grade: "<<grade<<endl;
      cout<<endl;
   }
};
int main()
{
    Student s1("raman",'B'),s2("joginder",'D'),s3("ranveer",'A');
    s1.display();
    s2.display();
    s3.display();

    return 0;
}