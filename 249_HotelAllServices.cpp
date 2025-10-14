//Wap to make a complete hotel facilities .
#include <iostream>
using namespace std;
class Breakfast
{
    string dish;
    int price;
public:
    Breakfast(string dish,int price)
    {
        this->dish=dish;
        this->price=price;
    }
    void display_Dishes()
    {
        cout<<dish<<"      "<<price<<endl;
    }
};
class Lunch
{
    string dish;
    int price;
public:
    Lunch(string dish,int price)
    {
        this->dish=dish;
        this->price=price;
    }
    void display_Dishes()
    {
        cout<<"Name: "<<dish<<endl;
        cout<<"Price: "<<price<<endl;
    }
};
class Dinner
{
    string dish;
    int price;
public:
    Dinner(string dish,int price)
    {
        this->dish=dish;
        this->price=price;
    }
    void display_Dishes()
    {
        cout<<"Name: "<<dish<<endl;
        cout<<"Price: "<<price<<endl;
    }
};
class Snacks
{
    string dish;
    int price;
public:
    Snacks(string dish,int price)
    {
        this->dish=dish;
        this->price=price;
    }
    void display_Dishes()
    {
        cout<<"Name: "<<dish<<endl;
        cout<<"Price: "<<price<<endl;
    }
};
int main()
{
    Breakfast a1("Paneer Paratha",80),a2("Aloo Paratha",60),a3("Veg Sandwich",50);
    Lunch b1("Veg Thali",150),b2("Idli Sambar",70),b3("Manchurien",90);
    Dinner c1("Fried Rice",120),c2("Biryani",130),c3("Mix Veg Pulao",110);
    Snacks d1("Paani puri",40),d2("Samosa",15),d3("Noodels",60);
    string choice;
    cout<<"=====!WELCOME/NAMASTE/PRANAM!====="<<endl;
    cout<<"Our hotel servises:- "<<endl;
    cout<<"1.Book a Room"<<endl;
    cout<<"2.Breakfast"<<endl;
    cout<<"3.Lunch"<<endl;
    cout<<"4.Dinner"<<endl;
    cout<<"5.Snacks"<<endl;
    cout<<"->";
    cin>>choice;
    if(choice=="Breakfast")
    {
        cout<<"DISH            PRICE"<<endl;
        a1.display_Dishes();
        a2.display_Dishes();
        a3.display_Dishes();
    }
    else if(choice=="Lunch")
    {
        cout<<"DISH            PRICE"<<endl;
        b1.display_Dishes();
        b2.display_Dishes();
        b3.display_Dishes();
    }
    else if(choice=="Dinner")
    {
        cout<<"DISH            PRICE"<<endl;
        c1.display_Dishes();
        c2.display_Dishes();
        c3.display_Dishes();
    }
    else if(choice=="Snacks")
    {
        cout<<"DISH            PRICE"<<endl;
        d1.display_Dishes();
        d2.display_Dishes();
        d3.display_Dishes();
    }
    else{
        cout<<"Invalid Input!"<<endl;
    }

    return 0;
}