#include<iostream>
using namespace std;
class supermarket
{
   string productName;
   int price;
public:
    void storage()
    {
        cout<<"enter product name: ";
        cin>>productName;
        cout<<"enter product price: ";
        cin>>price;
    }
    void display()
    {
          cout<<"product name: "<<productName<<endl;
          cout<<"price: "<<price<<endl;   
    }
};
int main()
{
    int i;
    supermarket product[4];
    for(i=0;i<4;i++)
    {
       product[i].storage();
    }
    cout<<"=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-"<<endl;
    for(i=0;i<4;i++)
    {
       product[i].display();
    }

    return 0;
}