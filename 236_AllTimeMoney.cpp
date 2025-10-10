//wap to make a ATM machine.
#include<iostream>
using namespace std;
class Accounts
{
    int acc_no;
    string name;
    float balance;
public:
    Accounts(int acc_no,string name,float balance)
    {
        this->acc_no=acc_no;
        this->name=name;
        this->balance=balance;
    }
    void display()
    {
        cout<<"ACCOUNT DETAILS"<<endl;
        cout<<"Owner name: "<<name<<endl;
        cout<<"Total balance: "<<balance<<endl;
        cout<<"Account number: "<<acc_no<<endl;
        cout<<"=========================="<<endl;
    }
    void withdraw(float amount)
    {
        if(amount>balance)
        {
            cout<<"Insufficient balance!"<<endl;
        }
        else{
            balance=balance-amount;
            cout<<"Please collect your cash!"<<endl;
            cout<<"Balance left: "<<balance<<endl;
        }
    }
    void deposit(float amount)
    {
        balance=balance+amount;
        cout<<"Your amount has been deposited successfully!"<<endl;
        cout<<"Balance left: "<<balance<<endl;
    }
};
int main()
{
    int acc;
    string choice;
    Accounts per1(2425686,"Sahaj Chhabra",50000.00);
    Accounts per2(2425687,"Jason Maxwell",60000.00);
    start:
    cout<<"=======WLCOME TO ATM MACHINE======="<<endl;
    cout<<"Enter your account number: ";
    cin>>acc;
    if(acc==2425686)
    {
        per1.display();
        start2:
        cout<<"1. Withdraw money"<<endl;
        cout<<"2. Deposit money"<<endl;
        cin>>choice;
        if(choice=="withdraw")
        {
            float money;
            cout<<"enter the amount: ";
            cin>>money;
            per1.withdraw(money);
        }
        else if(choice=="deposit")
        {
            float money;
            cout<<"enter the amount: ";
            cin>>money;
            per1.deposit(money);
            cout<<"Your amount has been deposited successfully!"<<endl;
        }
        else{
            cout<<"Invalid choice!"<<endl;
            goto start2;
        }
    }
    else if(acc==2425687)
    {
        per2.display();
        cout<<"1. Withdraw money"<<endl;
        cout<<"2. Deposit money"<<endl;
        cin>>choice;
    }
    else{
        cout<<"Invalid account number!"<<endl;
        goto start;
    }

    return 0;
}