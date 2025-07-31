#include<iostream>
using namespace std;
class office
{
    int no_employes;
    string boss;
    string name;
public:
    void set_office(int emp,string Boss,string nam)
    {
        no_employes=emp;
        boss=Boss;
        name=nam;
    }
    void display()
    {
        cout<<endl;
        cout<<"this is "<<name<<" office"<<endl;
        cout<<"this office has "<<no_employes<<" no. of employes"<<endl;
        cout<<"this office has a Boss named "<<boss<<endl;
        cout<<endl;
    }
};
int main()
{
    office vanguard,Nexsus;
    vanguard.set_office(45,"satyanarayana","vanguard");
    vanguard.display();
    Nexsus.set_office(56,"Keshav","Nexsus");
    Nexsus.display();

    return 0;
}