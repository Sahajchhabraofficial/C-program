//wap to check if a string is palindrome or not.
#include<iostream>
#include<string>
using namespace std;
int main()
{
    string str,rev="";
    int i;
    cout<<"Enter a string: ";
    cin>>str;//hello
    for(i=str.length();i<=0;i--)
    {
        cout<<str[i];
        
    }
    /*if(rev==str)
    {
        cout<<"string is palindrome";
    }
    else{
        cout<<"string is not palindrome";
    }*/

    return 0;
}