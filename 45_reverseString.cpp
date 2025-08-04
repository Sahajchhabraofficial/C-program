//wap to make a string reverse.
#include<iostream>
using namespace std;
int Reverse(string str)
{
    int i;
    int rev,length=0;
    for(i=0;i<='\0';i++)
    {
       length++;
    }
    for(i=0;i<=length;i++)
    {
        str[i]=str[length-i];
    }
    return rev;
}
int main()
{
    string name;
    cout<<"enter a string: ";
    cin>>name;//hello
    cout<<Reverse(name);
    
    return 0;
}