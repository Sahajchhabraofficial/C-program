//Print all multiples of a given number up to 100.
#include<iostream>
using namespace std;
int main()
{
    int i,num;
    cout<<"enter a number: ";
    cin>>num;//12
    for(i=1;;i++)
    {
          if(num*i>100)
          {
            break;
          }
        cout<<num*i<<" ";
  
    }

    return 0;
}