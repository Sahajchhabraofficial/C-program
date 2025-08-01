//wap to make a factorial calculator
#include <iostream>
using namespace std;
int factorial(int num)
{
    int i,fact=1;
    for(i=1;i<=num;i++)
    {
        fact=fact*i;
    }
    return fact;
}
int main()
{
    int n;
    cout<<"enter a number: ";
    cin>>n;
    cout<<factorial(n);

    return 0;
}