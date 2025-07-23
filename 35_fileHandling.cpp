//FILE HANDLING!
#include <iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream folder;
    int i,a,b;
    folder.open("sahaj.txt",std::_S_app);
    cout<<"enter a value: ";
    cin>>a;
    cout<<"entre b value: ";
    cin>>b;
    i=a+b;
    cout<<a<<" + "<<b<<" = "<<i;
    folder<<a<<" + "<<b<<" = "<<i<<endl;
    folder.close();

    return 0;
}