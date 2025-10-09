//checking different operators to overload.
#include<iostream>
using namespace std;
class Overloading
{
    int a;
    int b;
public:
    void operator<<(Overloading obj)
    {
        obj.a=a+obj.b;
        obj.b=b+obj.a;
    }
};
int main()
{
    Overloading ovr1,ovr2,ovr3;
    ovr1<<ovr2;

    return 0;
}