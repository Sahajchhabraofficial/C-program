//ARROW OPTEATOR POINTER IN CPP.
#include<iostream>
using namespace std;
class paisa
{
  int amount;
public:
    void set_paisa(int money)
    {
        amount=money;
    }
    void show_paisa()
    {
        cout<<"money balance: "<<amount<<endl;
    }
};
int main()
{
    paisa *ptr=new paisa;
    paisa obj;
    ptr=&obj;
    ptr->set_paisa(100000000);
    ptr->show_paisa();
    delete ptr;

    return 0;
}