//wap to genrate hollow square pattern: 
#include<iostream>
using namespace std;
int main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=5;j++)
        {
            if(i==2 && j==2)
            {
                cout<<"  ";
            }
            else if(i==3 && j==3)
            {
                cout<<"  ";
            }
            else if(i==4 && j==4)
            {
                cout<<"  ";
            }
            else if(i==2 && j==3)
            {
                cout<<"  ";
            }
            else if(i==3 && j==2)
            {
                cout<<"  ";
            }
            else if(i==4 && j==3)
            {
                cout<<"  ";
            }
            else if(i==3 && j==4)
            {
                cout<<"  ";
            }
            else if(i==2 && j==4)
            {
                cout<<"  ";
            }
            else if(i==4 && j==2)
            {
                cout<<"  ";
            }
            else{
                printf(" @");
            }
        }
        cout<<endl;
    }

    return 0;
}