//exapmlpe of a constructor.
#include <iostream>
using namespace std;
class house
{
    int price;
    string name;
public:
    house(){
        cout<<"this is a constructor"<<endl;
    }
    void set_house()
    {
        cout<<"this is a method"<<endl;
    }
};
int main()
{
    house h1,h2;
    h1.set_house();
    h2.set_house();
    return 0;
}