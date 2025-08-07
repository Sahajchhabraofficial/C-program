//wap to make a hollow square.
/* * * * * *
   *       *
   *       *
   *       *
   * * * * * 
*/
#include<iostream>
using namespace std;
int main()\
{
    int i,j,k;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=5;j++)
        {
            if(i==2 && j==2 || i==2 && j==3 || i==2 && j==4)
            {
                cout<<"  ";
            }
            else if(i==3 && j==2 || i==3 && j==3 || i==3 && j==4)
            {
                cout<<"  ";
            }
            else if(i==4 && j==2 || i==4 && j==3 || i==4 && j==4)
            {
                cout<<"  ";
            }
            else{
                cout<<" *";
            }
        }
        cout<<endl;
    }

    return 0;
}
