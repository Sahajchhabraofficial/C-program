//declearation of destructor.
#include<iostream>
using namespace std;
class pencil
{
  int price;
  string brand;
public:
    void set_pencil(int p,string br)
    {
        price=p;
        brand=br;
    }
    void get_pencil()
    {
        cout<<"PENCIL INFO:-"<<endl;
        cout<<"price: "<<price<<endl;
        cout<<"brand: "<<brand<<endl;
        cout<<"___________________"<<endl;
    }
    ~pencil()
    {
        cout<<"this is destructor"<<endl;
    }
    pencil()
    {
        cout<<"this is constructor"<<endl;
    }
};
int main()
{
    pencil p1,p2,p3;
    p1.set_pencil(12,"apsara");
    p2.set_pencil(10,"doms");
    p3.set_pencil(8,"natraj");
    p1.get_pencil();
    p2.get_pencil();
    p3.get_pencil();
}