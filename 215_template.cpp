//wap to return the greatest number of any data type.
#include<iostream>
using namespace std;
template<typename lo>
lo maxnum(lo num,lo nam)
{
    if(num>nam)
    {
        return num;
    }
    else{
        return nam;
    }
}
int main()
{
    int a,b;
    cout<<"enter anything: ";\
    cin>>a;
    cout<<"enter another anything: ";
    cin>>b;
    cout<<maxnum(a,b);

    return 0;
}