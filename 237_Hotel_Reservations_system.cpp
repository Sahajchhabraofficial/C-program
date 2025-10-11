//wap to make a Hotel Reservations system.
#include<iostream>
#include<random>
using namespace std;
class Hotel
{
    string name;
    int room_no;
    float rent=2500.00;
    int days;
    static int all_rooms;
public:
    void display()
    {
        cout<<"=-=-=-=-=-=-=-=-=-=-=-"<<endl;
        cout<<"GUEST DETAILS:-"<<endl;
        cout<<"Guest name: "<<name<<endl;
        cout<<"Room number: "<<room_no<<endl;
        cout<<"Rent: "<<rent<<endl;
        cout<<"=-=-=-=-=-=-=-=-=-=-=-"<<endl;
    }
    void Reservation(int num)
    {
        string nam;
        int roomNo;
        float ren;
        int day;
        cout<<"Enter your name: ";
        cin>>nam;
        cout<<"Your Room number: "<<num<<endl;
        cout<<"For how many days: ";
        cin>>day;
        ren=ren*day;
        cout<<"please pay: Rs."<<ren<<endl;
        name=nam;
        room_no=roomNo;
        ren=ren;
        days=day;
    }
    void cancel()
    {
        name="";
        room_no=0;
        rent=0;
        days=0;
        cout<<"Your reservation has been cancelled successfully!"<<endl;
    }
};
int Hotel::all_rooms=200;
int main()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1,200);
    int ROOM=distrib(gen);
    Hotel guest1;
    start:
    cout<<"=======WELCOME TO HOTEL RESERVATION SYSTEM======="<<endl;
    cout<<"Would you like to?: "<<endl;
    cout<<"1.Make a Reservation"<<endl;
    cout<<"2.Cancel a Reservation"<<endl;
    string choice;
    cout<<"->";
    cin>>choice;
    if(choice=="Reservation")
    {
        guest1.Reservation(ROOM);
        guest1.display();
    }
    else if(choice=="Cancel")
    {
        guest1.cancel();
        guest1.display();
    }
    else{
        cout<<"Feature not available!"<<endl;
        goto start;
    }

    return 0;
}