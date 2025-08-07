//wap to make a perfect triangle.
/*  *
   * * 
  * * * 
 * * * * 
* * * * * 
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
            if(i==1 && j==1)
            {
                cout<<"    ";
            }
            else if(i==2 && j==1)
            {
                cout<<"   ";
            }
            else if(i==3 && j==1)
            {
                cout<<"  ";
            }
            else if(i==4 && j==1)
            {
                cout<<" ";
            }
            cout<<" *";
        }
        cout<<endl;
    }

    return 0;
}