//wap to check which number is largest from given three.
#include<iostream>
using namespace std;
int main()
{
    int a,b,c;
    cout<<"enter a number: ";
    cin>>a;
    cout<<"enter another number: ";
    cin>>b;
    cout<<"enter another number: ";
    cin>>c;
    if(a>b && a>c)
    {
        cout<<a<<" is bigger"<<endl;
    }
    else if(b>c)
    {
        cout<<b<<" is bigger"<<endl;
    }
    else{
        cout<<c<<" is bigger"<<endl;
    }

    return 0;
}