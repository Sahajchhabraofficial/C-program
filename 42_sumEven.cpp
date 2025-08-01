//wap to sum of all digits between 1 to n.
#include<iostream>
using namespace std;
int sumEven(int n)
{
   int i;
   int number=0;
   for (i=1;i<=n;i++)
   {
      if(i%2==0)
      {
        number=number+i;
      }
   }
   return number;
}
int main()
{
    int num;
    cout<<"enter a number: ";
    cin>>num;
    cout<<sumEven(num);

    return 0;
}