//LIBRARY SYSTEM IN CPP.
#include <iostream>
using namespace std;
void reception()
{
    while(1)
    {
    string status;
     cout<<"would you like to?:-"<<endl;
     cout<<"Issue this book"<<endl;
     cout<<"purchase this book"<<endl;
     cout<<"->";
     cin>>status;
     if(status=="issue")
     {
        string name;
        string address;
        int age;
        int number;
        int days;
        cout<<"enter your name: ";
        cin>>name;
        cout<<"enter your address: ";
        cin>>address;
        cout<<"enter your age: ";
        cin>>age;
        cout<<"enter your contact number: ";
        cin>>number;
        cout<<"enter the number of days you issued: ";
        cin>>days;
        cout<<"your book is finnaly issued";
        break;
     }
     else if(status=="purchase")
     {
        string name;
        string address;
        int age;
        int number;
        cout<<"enter your name: ";
        cin>>name;
        cout<<"enter your address: ";
        cin>>address;
        cout<<"enter your age: ";
        cin>>age;
        cout<<"enter your contact number: ";
        cin>>number;
        cout<<"your Book is finally purchased";
        break;
     }
    }
}
void Selfhelp()
{
    string choice;
   cout<<"---------these are some self help books:----------"<<endl;
   cout<<"how to win friends and influence people"<<endl; 
   cout<<"power of subconcious mind"<<endl;
   cout<<"rewirw your habits"<<endl;
   cout<<"atomic habits"<<endl;
   cout<<"->";
   cin>>choice;
   cout<<"you choosed: "<<choice;
   reception();
}
void Fictional()
{
    string choice;
   cout<<"---------these are some fictional books:----------"<<endl;
   cout<<"harry potter"<<endl; 
   cout<<"secrete of the garden"<<endl;
   cout<<"king of hemisphere"<<endl;
   cout<<"Odyssy"<<endl;
   cout<<"->";
   cin>>choice;
   reception();
    
}
void Horror()
{
    string choice;
   cout<<"---------these are some horror books:----------"<<endl;
   cout<<"the clown"<<endl; 
   cout<<"we are never afraid to die"<<endl;
   cout<<"The silent voice"<<endl;
   cout<<"the grevyard"<<endl;
   cout<<"->";
   cin>>choice;
   reception();
}
void Fantasy()
{
    string choice;
   cout<<"---------these are some fantasy books:----------"<<endl;
   cout<<"Demon slayer"<<endl; 
   cout<<"joulis lake"<<endl;
   cout<<"the lion behind bars"<<endl;
   cout<<"french armies VII"<<endl;
   cout<<"->";
   cin>>choice;
   reception();
}
int main()
{   
    string choice;
    cout<<"=-=-=-WELCOME TO SANSKAAR LIBRARY=-=-=-"<<endl;
    cout<<"what category book do you want?: ";
    cin>>choice;
    if(choice=="selfhelp")
    {
        Selfhelp();
    }
    else if(choice=="fictional")
    {
        Fictional();
    }
    else if(choice=="fantasy")
    {
        Fantasy();
    }
    else if(choice=="horror")
    {
        Horror();
    }
    else{
        cout<<"category not available"<<endl;
    }

    return 0;
} 