//TEMPLATE!
#include<iostream>
using namespace std;
template<class data1,class data2>
class super
{
   data1 var1;
   data1 var2;
public: 
    super(data1 var1,data2 var0)
    {
        this->var1=var0;
        this->var2=var1;
    }
    void display()
    {
        cout<<endl;
        cout<<"variable 1 value: "<<var1<<endl;
        cout<<"variable 2 value:  "<<var2<<endl;
        cout<<endl;
    }
};
int main()
{
    super<string,int> obj("mustang",322);
    obj.display();
    super<int,float> obj2(351,45.2);
    obj2.display();
    super<int,char> obj3(315,'H');
    obj3.display();

    return 0;
}