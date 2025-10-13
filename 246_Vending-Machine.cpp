//wap to create a vending machine.
#include <iostream>
using namespace std;
int Payment(int item, int quan)
{
    int price;
    switch(item)
    {
        case 1:
            price=20*quan;
            break;
        case 2:
            price=30*quan;
            break;
        case 3:
            price=40*quan;
            break;
        case 4:
            price=10*quan;
            break;
        default:
            price=0;
    }
    return price;
}
int main()
{
    start:
    int payment;
    int quan;
    int item;
    string choice1, choice2, choice3, choice4;
    cout<<"-======-Vending machine-======-"<<endl;
    cout<<"   Items               Price   "<<endl;  
    cout<<"1. Chips               Rs.20      "<<endl;
    cout<<"2. Chocolate           Rs.30      "<<endl;
    cout<<"3. Cold drink          Rs.40      "<<endl;
    cout<<"4. Biscuits            Rs.10      "<<endl;
    cout<<"5. Exit                        "<<endl;
    cout<<"-> ";
    cin>>item;
    cout<<"How much quantity? ";
    cin>>quan;
    switch(item)
    {
        case 1:
            cout<<"You have selected "<<quan<<" Chips."<<endl;
            payment1:
            cout<<"Total price is:Rs."<<20*quan<<endl;
            cout<<"->";
            cin>>payment;
            if(payment<Payment(1,quan))
            {
                cout<<"Insufficient amount!"<<endl;
                goto payment1;
            }
            else if(payment>Payment(1,quan))
            {
                int change;
                payment=payment-Payment(1,quan);
                cout<<"This is your change:Rs."<<payment<<endl;
            }
            cout<<"Want to buy more? ";
            cin>>choice1;
            if(choice1=="yes")
            {
                goto start;
            }
            cout<<"Thank you!"<<endl;
            break;
        case 2:
            cout<<"You have selected "<<quan<<" Chocolate."<<endl;
            payment2:
            cout<<"Total price is:Rs."<<30*quan<<endl;
            cout<<"->";
            if(payment<Payment(2,quan))
            {
                cout<<"Insufficient amount!"<<endl;
                goto payment2;
            }
            else if(payment>Payment(2,quan))
            {
                int change;
                payment=payment-Payment(2,quan);
                cout<<"This is your change:Rs."<<payment<<endl;
            }
            cout<<"Want to buy more? ";
            cin>>choice2;
            if(choice2=="yes")
            {
                goto start;
            }
            cout<<"Thank you!"<<endl;
            break;
        case 3:
            cout<<"You have selected "<<quan<<" Cold drink."<<endl;
            payment3:
            cout<<"Total price is:Rs."<<40*quan<<endl;
            cout<<"->";
            cin>>payment;
            if(payment<Payment(3,quan))
            {
                cout<<"Insufficient amount!"<<endl;
                goto payment3;
            }
            else if(payment>Payment(3,quan))
            {
                int change;
                payment=payment-Payment(3,quan);
                cout<<"This is your change:Rs."<<payment<<endl;
            }
            cout<<"Want to buy more? ";
            cin>>choice3;
            if(choice3=="yes")
            {
                goto start;
            }
            break;
        case 4:
            cout<<"You have selected "<<quan<<" Biscuits."<<endl;
            payment4:
            cout<<"Total price is:Rs."<<10*quan<<endl;
            cout<<"->";
            cin>>payment;
            if(payment<Payment(4,quan))
            {
                cout<<"Insufficient amount!"<<endl;
                goto payment4;
            }
            else if(payment>Payment(4,quan))
            {
                int change;
                payment=payment-Payment(4,quan);
                cout<<"This is your change:Rs."<<payment<<endl;
            }
            cout<<"Want to buy more? ";
            cout<<"Want to buy more? ";
            cin>>choice4;
            if(choice4=="yes")
            {
                goto start;
            }
        case 5:
            cout<<"Thank you!"<<endl;
            break;
        default:
            cout<<"Invalid input!"<<endl;
    }

    return 0;
}