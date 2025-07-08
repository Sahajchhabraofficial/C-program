//FRIEND FUNCTION
#include<iostream>
using namespace std;
class base
{
   int num1;
   int num2;
public: 
    friend void dost(base);
    void add(int a,int b)
    {
        int res;
        num1=a;
        num2=b;
        res=num1+num2;
    }

};
void dost(base ans)
{
   cout<<"PRIVATE DATA:- "<<endl;
   cout<<"num1: "<<ans.num1<<endl;
   cout<<"num2: "<<ans.num2<<endl;
}
int main()
{
    base b1;
    b1.add(52,96);
    dost(b1);

    return 0;
}