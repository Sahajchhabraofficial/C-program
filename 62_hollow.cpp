//wap to make a inverted right hollow pyramid.
/* *****
   *  *
   * *
   **
   * 
*/ 
#include<iostream>
using namespace std;
int main()
{ 
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=5;j>=i;j--)
        {
            if(j==3 && i==2 || i==2 && j==4 || i==3 && j==4)
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
