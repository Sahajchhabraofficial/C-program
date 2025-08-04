//wap which calculates the area of rectangle
#include<iostream>
using namespace std;
class Rectangle
{
   int width;
   int height;
public:
    Rectangle(int wid,int hei)
    {
        width=wid;
        height=hei;
    }
    void calculateArea()
    {
        int area;
        area=width*height;
        cout<<"area of the rectangle is "<<area<<endl;;
    }
};
int main()
{
    Rectangle r1(12,62),r2(16,65);
    r1.calculateArea();
    r2.calculateArea();

    return 0;
}