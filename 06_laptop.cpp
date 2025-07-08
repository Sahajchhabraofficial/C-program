//wap to make a class for laptop.
#include<iostream>
using namespace std;
class laptop
{
   int price;
   string name;
   string model;
public:
      void set_laptop(int p,string nam,string mod)
      {
        name=nam;
        model=mod;
        price=p;
      }
      void get_laptop()
      {
        cout<<"LAPTOP INFO:- "<<endl;
        cout<<"laptop model name: "<<model<<endl;
        cout<<"laptop price: "<<price<<endl;
        cout<<"laptop bbrand: "<<name<<endl;
        cout<<"--------------------------"<<endl;
      }
};
int main()
{
    laptop HP,Dell,Lenovo;
    HP.set_laptop(65000,"HP","victus");
    Dell.set_laptop(45000,"Dell","inspiron");
    Lenovo.set_laptop(56000,"Lenovo","LOQ");
    HP.get_laptop();
    Dell.get_laptop();
    Lenovo.get_laptop();
}
