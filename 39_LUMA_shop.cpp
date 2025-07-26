//LUMA!
#include<Iostream>
using namespace std;
void bag()
{
   cout<<"welcome to gym bag"<<endl;
}
void socks()
{
     cout<<"welcome to socks"<<endl;
}
void gloves()
{
     cout<<"welcome to gloves"<<endl;
}
void cap()
{
     cout<<"welcome to cap"<<endl;
}
int main()
{
    string buyer;
    cout<<"============welcome to LUMA's showroom============"<<endl;
    cout<<"what do you like to buy?"<<endl;
    cout<<"->";
    cin>>buyer;
    if(buyer=="bag")
    {
       bag();
    }
    else if(buyer=="gloves")
    {
        gloves();
    }
    else if(buyer=="cap")
    {
        cap();
    }
    else if(buyer=="socks")
    {
        socks();
    }
    else{
        cout<<"!!item not available!!"<<endl;
    }

    return 0;
}