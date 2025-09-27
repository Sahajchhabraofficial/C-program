//wap that find the area of circle using operator overloading.
#include<iostream>
using namespace std;
class Area
{
    int length;
    int width;
    int height;
    int radius;
    int base;
    int result;
public:
    Area(){}
    Area(int radius)
    {
        this->radius=radius;
    }
    Area(int length)
    {
        this->length=length;
    }
    Area(int height)
    {
        this->height=height;
    }
    Area(int width)
    {
        this->width=width;
    }
    Area(int base)
    {
        this->base=base;
    }
    Area operator*(Area obj)
    {
        Area result;
        obj.result=radius*obj.radius*obj.radius;
        obj.result=obj.length*obj.width;
        obj.result=obj.base*obj.height;
    }
};
int main()
{
    Area radius(62),length(95),base(24),height(52),width(35),triangle,rectangle,circle;
    circle=radius*radius;
    rectangle=length*width;
    triangle=base*height;

    return;
}