//BASIC BANK ACCOUNT!
#include<iostream>
using namespace std;
class BankAccount
{
   int balance=50000;
public:
    void deposit(double amount)
    {
        if(balance>amount)
        {
            balance-amount;
            cout<<amount<<" deposited successfully!"<<endl;
        }
        else{
            cout<<"issuficient money in account!"<<endl;
        }
    }
    void withdraw(double amount)
    {
        balance+amount;
        cout<<amount<<" deposited successfully!"<<endl;
    }
};
int main()
{
    BankAccount person1,person2;
    person1.deposit(13000);
    person2.withdraw(45000);

    return 0;
}