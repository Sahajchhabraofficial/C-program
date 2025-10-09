//wap to check if a password meets it's ctiteria or not.
#include<iostream>
using namespace std;
int length(string str)
{
    return str.size();
}
int main()
{
    start:
    int i;
    string password;
    cout<<"enter a password: ";
    cin>>password;
    if(length(password)<8)
    {
        cout<<"The Password should contain at least 8 characters!"<<endl;
        goto start;
    }
    else if(length(password)>=8)
    {
        for(i=0;i<=(8+(length(password)-8));i++)
        {
            if(password[i]<='A' && password[i]>='Z')
            {
                cout<<"The Password should contain at least one uppercase letter!"<<endl;
                goto start;
            }
            else if(password[i]<='a' && password[i]>='z')
            {
                cout<<"The Password should contain at least one lowercase letter!"<<endl;
                goto start;
            }
            else if(password[i]<='0' && password[i]>='9')
            {
                cout<<"The Password should contain at least one digit!"<<endl;
                goto start;
            }
            else if(password[i]=='@' || password[i]=='#' || password[i]=='$' || password[i]=='%' || password[i]=='&' || password[i]=='*')
            {
                cout<<"The Password should contain at least one special character!"<<endl;
                goto start;
            }
        }
    }

    return 0;
}