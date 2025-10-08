#include<iostream>
using namespace std;
class XIA
{
    string name;
    int rollnumber;
public:
    XIA(string name,int rollnumber)
    {
        this->name=name;
        this->rollnumber=rollnumber;
    }
    void display()
    {
        cout<<"STUDENT DETAILS:-"<<endl;
        cout<<"name: "<<name<<endl;
        cout<<"Roll number: "<<rollnumber<<endl;
        cout<<"=-=-=-=-=-=-=-=-=-"<<endl;
    }
    ~XIA(){}
};
int main()
{
    XIA std1("Raj",11124),std2("Sahaj",11125),std3("Sandesh",11127);
    std1.display();
    std2.display();
    std3.display();

    return 0;
}