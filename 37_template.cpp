//TEMPLATE!
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream usdollars;
    usdollars.open("sahaj.txt");
    string read;
    usdollars>>read;
    cout<<read;
    int i;
    for (i=1;i=='\0';i++)
    {
       usdollars>>read;
    }
    for (i=1;i=='\0';i++)
    {
       cout<<read;
    }

    usdollars.close();
    return 0;
}