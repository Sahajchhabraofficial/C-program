//Calculate the result of following series:
//(1+2)*(3+4)*(5+6)*. . . . . . . . . upto 10 terms.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=1,inc=1,inr=2;
    for(i=1;i<=10;i++)
    {
       sum=sum*(inc+inr);
       inc++;
       inr++;
    }
    cout<<endl;
    cout<<sum;

    return 0;
}