//waf which count how many times did a character appears in the string.
#include<iostream>
using namespace std;
int countChar(string str,char c)
{
    int i,count;
    for(i=0;i<=10;i++)
    {
        if(str[i]==c)
        {
           count++;
        }
    }
    return count;
}
int main()
{
    string name;
    char len;
    cout<<"enter a string: ";
    cin>>name;
    cout<<"what char should count: ";
    cin>>len;
    cout<<countChar(name,len)-1;

    return 0;
}