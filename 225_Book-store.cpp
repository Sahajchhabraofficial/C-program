//Create a class Book with attributes title, author, and price. Store details of 5 books and display the book with the highest price
#include<iostream>
using namespace std;
class Bookstore
{
    string title;
    string author;
    int price;
public:
    Bookstore(string title,string author,int price)
    {
        this->title=title;
        this->author=author;
        this->price=price;
    }
    void display()
    {
        cout<<"||/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/||"<<endl;
        cout<<"||BOOK WITH THE HEIGHEST PRICE:- ||"<<endl;
        cout<<"||title: "<<title<<"              ||"<<endl;
        cout<<"||author: "<<author<<"      ||"<<endl;
        cout<<"||price: "<<price<<"                    ||"<<endl;
        cout<<"||/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/||"<<endl;
    }
};
int main()
{
    Bookstore book1("harry potter","J.K.Rowling",350);
    Bookstore book2("fairy tales","Lewis Carroll",400);
    Bookstore book3("Discovery of India","Jawaharlal Nehru",240);
    Bookstore book4("Elden Ring","George R.R.Martin",2215);
    Bookstore book5("The Secret","Rhonda Byrne",90);
    book4.display();

    return 0;
}