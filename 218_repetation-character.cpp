//wap to check the repetation of a character in a string.
#include<iostream>
using namespace std;
int main()
{
    string str="Hello World";
    int count=0,i;
    char caracter;
    cout<<"enter a character: ";
    cin>>caracter;
    for(i=1;i<=11;i++)
    {
        if(caracter==str[i])
        {
            count++;
        }
    }
    cout<<"the "<<caracter<<" repeats "<<count<<" times"<<endl;

    return 0;
}