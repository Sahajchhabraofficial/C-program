//wap to make a restraunt table mangement system design.
#include <iostream>
using namespace std;
class Tables
{
    int members;
    int number;
    string status;
public:
    Tables(int members, int number,string status)
    {
        this->members=members;
        this->number=number;
        this->status=status;
    }
    void Details()
    {
        cout<<"TABLE INFO:-"<<endl;
        cout<<"Table number: "<<number<<endl;
        cout<<"Members: "<<members<<endl;
        cout<<"Status: "<<status<<endl;
        cout<<"============================"<<endl;
    }
    bool Availability()
    {
        if(status=="available")
        {
            return true;
        }
        else{
            return false;
        }
    }
};
int main()
{
    Tables a1(2,1,"available");
    Tables a2(2,2,"not available");
    Tables a3(3,3,"available");
    Tables a4(3,4,"not available");
    Tables a5(6,4,"available");
    Tables a6(6,5,"not available");
    Tables a7(5,6,"available");
    Tables a8(5,4,"not available");
    string choice;
    int peoples;
    cout<<"========WELCOME TO OUR RESTRAUNT========"<<endl;
    cout<<"would you like to?"<<endl;
    cout<<"1.Book a table"<<endl;
    cout<<"2.Check available tables"<<endl;
    cout<<"->";
    cin>>choice;
    if(choice=="Book")
    {
        cout<<"How many peoples are you?";
        cin>>peoples;
        switch(peoples)
        {
            case 2:
                if(a1.Availability())
                {
                    cout<<"Table 1 is booked for you."<<endl;
                }
                else if(a2.Availability())
                {
                    cout<<"Table 2 is booked for you."<<endl;
                }
                else{
                    cout<<"Sorry! No table available for 2 peoples."<<endl;
                }
                break;
            case 3:
                if(a3.Availability())
                {
                    cout<<"Table 3 is booked for you."<<endl;
                }
                else if(a4.Availability())
                {
                    cout<<"Table 4 is booked for you."<<endl;
                }
                else{
                    cout<<"Sorry! No table available for 3 peoples."<<endl;
                }
                break;
            case 5:
                if(a7.Availability())
                {
                    cout<<"Table 7 is booked for you."<<endl;
                }
                else if(a8.Availability())
                {
                    cout<<"Table 8 is booked for you."<<endl;
                }
                else{
                    cout<<"Sorry! No table available for 5 peoples."<<endl;
                }
            case 6:
                if(a5.Availability())
                {
                    cout<<"Table 5 is booked for you."<<endl;
                }
                else if(a6.Availability())
                {
                    cout<<"Table 6 is booked for you."<<endl;
                }
                else{
                    cout<<"Sorry! No table available for 6 peoples."<<endl;
                }
                break;
            default: cout<<"Too much members!"<<endl;
        }
    }
    else if(choice=="Check")
    {
        a1.Details();
        a2.Details();
        a3.Details();
        a4.Details();
        a5.Details();
        a6.Details();
        a7.Details();
        a8.Details();
    }
    else{
        cout<<"Invalid Input!"<<endl;
    }

    return 0;
}