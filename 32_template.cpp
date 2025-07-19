//TEMPLATE!
#include<iostream>
using namespace std;
template<class data>
class father
{
  data number;
public:
    father(data var)
    {
        number=var;
    }
    void display()
    {
        cout<<"number: "<<number<<endl;
    }
};
int main()
{
    father<int> f1(65);
    f1.display();
    father<string>f2("sahaj");
    f2.display();

    return 0;
}