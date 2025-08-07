//wap to make a pattern of hollow triangle.
/* * 
   ** 
   * * 
   *  * 
   *****
*/
#include<iostream>
using namespace std;
int main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=i;j++)
        {
            if(i==3 && j==2 || j==2 && i==4 || j==3 && i==4)
            {
              cout<<" ";
            }
            else{
              cout<<"*";
            }
        }
        cout<<endl;
    }

    return 0;
}