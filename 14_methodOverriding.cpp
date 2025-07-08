//method overriding 
#include <iostream>
using namespace std;
class father 
{
   /*data members*/
public:
    void method()
    {
        cout<<"this is a method of father"<<endl;
    }
};
class child:public father
{
   /*data members*/
public:
    void method()//overrided method 
    {
        cout<<"this is a method of child"<<endl;
    }
};
int main()
{
    child c2;
    c2.method();

    return 0;

}
