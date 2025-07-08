//wap to make a constructor .
#include<iostream>
using namespace std;
class bottle
{
  int price;
  float space;
  string name;
public:
      void set_bottle(int p,string nam,float spac)
      {
        name=nam;
        price=p;
        space=spac;
      }
      void get_bottle()
      {
        cout<<"BOTTLE INFO:- "<<endl;
        cout<<"NAME: "<<name<<endl;
        cout<<"PRICE: "<<price<<endl;
        cout<<"SPACE: "<<space<<"liters"<<endl;
        cout<<"_______________"<<endl;
      }
};
int main()
{
    bottle b1,b2,b3;
    b1.set_bottle(250,"Milton",1.43);
    b2.set_bottle(350,"Pexpo",1.5);
    b3.set_bottle(525,"Cello",2.3);
    b1.get_bottle();
    b2.get_bottle();
    b3.get_bottle();
}