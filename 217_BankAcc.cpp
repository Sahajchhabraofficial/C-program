//wap to make a class for bank accounts.
#include<iostream>
using namespace std;
class BankAccount
{
    int balance;
    string name;
public:
    BankAccount(int balance,string name)
    {
        this->balance=balance;
        this->name=name;
    }
    void display()
    {
        cout<<"BANK ACCOUNT DETAILS:-"<<endl;
        cout<<"name: "<<name<<endl;
        cout<<"balance: "<<balance<<endl;
        cout<<"=-=-=-=-=-=-=-=-=-=-="<<endl;
    }
    void credit()
    {
        int amount;
        cout<<"what amount should credit?";
        cin>>amount;
        balance=balance+amount;
    }
    void debdit()
    {
        int amount;
        cout<<"what amount should debdit?";
        cin>>amount;
        balance=balance-amount;
    }
};
int main()
{
    BankAccount acc1(50000,"rajesh"),acc2(25000,"mukesh");
    string status,name;
    cout<<"enter account name: ";
    cin>>name;
    if(name=="rajesh")
    {
        cout<<"Debit or Credit?";
        cin>>status;
        if(status=="Credit")
        {
            acc1.credit();
            acc1.display();
        }
        else{
            acc2.debdit();
            acc1.display();
        }
    }
    else if(name=="mukesh")
    {
        cout<<"Debit or Credit?";
        cin>>status;
        if(status=="Credit")
        {
            acc2.credit();
            acc2.display();
        }
        else{
            acc2.debdit();
            acc2.display();
        }
    }

    return 0;
}