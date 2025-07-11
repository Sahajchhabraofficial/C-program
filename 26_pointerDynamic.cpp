//pointre with a constructor.
#include <iostream>
using namespace std;
class gaddi
{
   int price;
public: 
    gaddi(int a)
    {
        price=a;
    }
    void display()
    {
        cout<<"PRICE= "<<price<<endl;
    }
};
int main()
{
    gaddi *ptr=new gaddi(5000000);
    ptr->display();
    delete ptr;
    return 0;
}
