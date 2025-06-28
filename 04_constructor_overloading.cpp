//Overloading constructors.
#include <iostream>
using namespace std;
class watch
{
   int price;
   string brand;
public:
    watch(int p)
    {
        cout<<"this is one argument constructor"<<endl;
    }
    watch()
    {
        cout<<"this is zero argument constructor"<<endl;
    }
    watch(float rating, string name)
    {
        cout<<"this is two argument constructor"<<endl;
    }
    watch(string style, string naame, int quantity)
    {
        cout<<"this is three argument constructor"<<endl;
    }
};
int main()
{
   watch apple();
   watch fastrack(3000);
   watch fireboult(4.8,"visinory");
   watch rolex("sports","daytona",500);
   return 0;
}