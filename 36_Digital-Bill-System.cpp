//DIGITAL BILL APPLICATIOIN!
#include<iostream>
#include<fstream>
using namespace std;
class accounts
{
   int password;
   string name;
public:
    void login()
    {
        start:
        cout<<"enter your name: ";
        cin>>name;
        cout<<"enter your passsword: ";
        cin>>password;
        if(password==23265554)
        {
          cout<<"----You are successfully login----"<<endl;
        }
        else{
            cout<<"You are not the owner please try again!"<<endl;
            goto start;
        }
    }
};
int main()
{
    ofstream record;
    int password;
    string name;
    string exit;
    record.open("book of original entry.txt",std::_S_app);
    cout<<"----To use our app please verify first----"<<endl;
    accounts user1;
    user1.login();
   string product;
   string category;
   float price;
   int amount;
   while(1)
   {
     cout<<"enter product name: ";
     cin>>product;
     cout<<"enter product amount: ";
     cin>>amount;
     cout<<"enter product category: ";
     cin>>category;
     cout<<"enter product price: ";
     cin>>price;
     cout<<"adding more products: ";
     cin>>exit;
     record<<"|  "<<product<<"   |  "<<amount<<"kg  |  "<<category<<"  |  ₹"<<price<<"  |  "<<price*amount<<"  |"<<endl;
     if(exit=="no" || exit=="No")
     {
        break;
     }
   }
   cout<<"=-=-=-=-=-=-=-=-=-=your bill is successfully added=-=-=-=-=-=-=-=-=-="<<endl;
   record.close();

    return 0;
}