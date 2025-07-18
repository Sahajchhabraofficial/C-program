//VISIBLITY MODE!
//PUBLIC:
#include<iostream>
using namespace std;
class demo
{
    int number;
public: 
    demo(int a)
    {
        number=a;
    } 
    void display()
    {
        cout<<"number= "<<number<<endl;
    }
}; 
class derived :public demo
{
   //code// 
};
int main()
{
    demo d1(52);
    d1.display();

    return 0;
}