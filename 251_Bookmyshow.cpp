//wap to clone Book my show app features.
//ADDING PAYMENT SYSTEM IS REMAINING...
#include<iostream>
using namespace std;
class Recent_Shows
{
    string Show_name;
    float Ticket_price;
    int available_seats;
public:
    Recent_Shows(){}
    Recent_Shows(string Show_name,float Ticket_price,int available_seats)
    {
        this->Show_name=Show_name;
        this->Ticket_price=Ticket_price;
        this->available_seats=available_seats;
    }
    void display_shows()
    {
        if(Show_name!="empty" && Ticket_price!=0 && available_seats!=0)
        {
            cout<<"/*/*/*/*/*/*/*/*/*/*/*/*/"<<endl;
            cout<<"Show name: "<<Show_name<<endl;
            cout<<"Ticket price: "<<Ticket_price<<endl;
            cout<<"available seats: "<<available_seats<<endl;
        }
    }
    void add_shows()
    {
        if(Show_name=="empty" && Ticket_price==0 && available_seats==0)
        {
            cout<<"Enter show name: ";
            cin>>Show_name;
            cout<<"Enter ticket price: ";
            cin>>Ticket_price;
            cout<<"Enter available seats: ";
            cin>>available_seats;
        }
    }
    void delete_shows()
    {
        Show_name="empty";
        Ticket_price=0;
        available_seats=0;
        cout<<"Show deleted!"<<endl;;
    }
};
int main()
{
    start:
    Recent_Shows show1("Kantara",200,50),show2("War2",205,15),show3("Coolie",580,12),show4("empty",0,0),show5("empty",0,0);
    string choice;
    cout<<"===================WELCOME==================="<<endl;
    cout<<"!You have find perfect place to book your show!"<<endl;
    cout<<"Would you like to?"<<endl;
    cout<<"1.Book a selected show"<<endl;
    cout<<"2.See your ticket"<<endl;
    cout<<"3.Checkout Recent shows"<<endl;
    cout<<"->";
    cin>>choice;
    if(choice=="Book")
    {
        /*code*/
    }
    else if(choice=="Ticket")
    {
        /*code*/
    }
    else if(choice=="staff")
    {
        string ch;
        cout<<"Add shows or delete shows?";
        cin>>ch;
        if(ch=="add")
        {
            char more;
            show4.add_shows();
            cout<<"add more shows?";
            cin>>more;
            if(more=='y')
            {
                show5.add_shows();
            }
        }
        else if(ch=="delete")
        {
            char ch;
            show1.delete_shows();
            cout<<"delete more?";
            cin>>ch;
            if(ch=='y')
            {
                char ch2;
                show2.delete_shows();
                cout<<"delete more?";
                cin>>ch2;
                if(ch2=='y')
                {
                    show3.delete_shows();
                }
            }
        }
    }
    else if(choice=="Checkout")
    {
        int show;
        show1.display_shows();
        show2.display_shows();
        show3.display_shows();
        show4.display_shows();
        show5.display_shows();
        cout<<"Which show do you want to book?";
        cin>>show;
        cout<<"        !!Congratulations!!"<<endl;
        cout<<"========your show is booked========";
    }
    else{
        cout<<"Feature not available!";
        goto start;
    }

    return 0;
}