//wap to make a inverted pryamid of numbers(horizontally).
#include <iostream>
using namespace std;
int main()
{
    int i,j;
    for(i=1;i<=5;i++)
    {
        for(j=5;j>=i;j--)
        {
            cout<<" "<<i;
        }
        cout<<endl;
    }

    return 0;
}