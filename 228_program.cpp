#include<iostream>
using namespace std;
int main()
{
    int a,b,c;
    cout<<"Enter three numbers: ";
    cin>>a>>b>>c;
    if(a>b && a>c)
    {
        cout<<"largest number: "<<a;
    }
    else if(b>c)
    {
        cout<<"Largest numebr: "<<b;
    }
    else{
        cout<<"Largest number: "<<c;
    }
    
    return 0;
}