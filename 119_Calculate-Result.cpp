//Calculate the result of following series:
//(1+2)/(2+3)+(3+4)/(4+5) +. . . . . . . . . upto 10 terms.
#include<iostream>
using namespace std;
int main()
{
    int i,sum=1,inc=2;
    for(i=1;i<=10;i++)
    {
        sum=sum/(i+inc);
        inc++;
        cout<<sum<<" ";
    }
    cout<<endl;
    cout<<sum;

    return 0;
}