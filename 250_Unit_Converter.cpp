//wap to make a unit concerter.
#include<iostream>
using namespace std;
class UnitConverter
{
    int Main_unit;
    string Conv_unit;
public:
    UnitConverter(int Main_unit,string Conv_unit)
    {
        this->Main_unit=Main_unit;
        this->Conv_unit=Conv_unit;
    }
    int Length(string to_which)
    {
        if(Conv_unit=="cm" && to_which=="m")
        {
            return Main_unit/100;
        }
        else if(Conv_unit=="m" && to_which=="cm")
        {
            return Main_unit*100;
        }
        else if(Conv_unit=="km" && to_which=="m")
        {
            return Main_unit*1000;
        }
        else if(Conv_unit=="m" && to_which=="km")
        {
            return Main_unit/1000;
        }
        else if(Conv_unit=="cm" && to_which=="km")
        {
            return Main_unit/100000;
        }
        else if(Conv_unit=="km" && to_which=="cm")
        {
            return Main_unit*100000;
        }
        else if(Conv_unit=="inch" && to_which=="cm")
        {
            return Main_unit*2.54;
        }
        else if(Conv_unit=="cm" && to_which=="inch")
        {
            return Main_unit/2.54;
        }
        else
        {
            return -1;
        }
    }
    int Weight(string to_which)
    {
        if(Conv_unit=="g" && to_which=="kg")
        {
            return Main_unit/1000;
        }
        else if(Conv_unit=="kg" && to_which=="g")
        {
            return Main_unit*1000;
        }
        else if(Conv_unit=="mg" && to_which=="g")
        {
            return Main_unit/1000;
        }
        else if(Conv_unit=="g" && to_which=="mg")
        {
            return Main_unit*1000;
        }
        else if(Conv_unit=="kg" && to_which=="mg")
        {
            return Main_unit*1000000;
        }
        else if(Conv_unit=="mg" && to_which=="kg")
        {
            return Main_unit/1000000;
        }
        else
        {
            return -1;
        }
    }
    int Temperature(string to_which)
    {
        if(Conv_unit=="C" && to_which=="F")
        {
            return (Main_unit*9/5)+32;
        }
        else if(Conv_unit=="F" && to_which=="C")
        {
            return (Main_unit-32)*5/9;
        }
        else if(Conv_unit=="C" && to_which=="K")
        {
            return Main_unit+273.15;
        }
        else if(Conv_unit=="K" && to_which=="C")
        {
            return Main_unit-273.15;
        }
        else if(Conv_unit=="F" && to_which=="K")
        {
            return (Main_unit-32)*5/9+273.15;
        }
        else if(Conv_unit=="K" && to_which=="F")
        {
            return (Main_unit-273.15)*9/5+32;
        }
        else
        {
            return -1;
        }
    }
    int Currency(string to_which)
    {
        if(Conv_unit=="USD" && to_which=="INR")
        {
            return Main_unit*82;
        }
        else if(Conv_unit=="INR" && to_which=="USD")
        {
            return Main_unit/82;
        }
        else if(Conv_unit=="EUR" && to_which=="INR")
        {
            return Main_unit*88;
        }
        else if(Conv_unit=="INR" && to_which=="EUR")
        {
            return Main_unit/88;
        }
        else if(Conv_unit=="GBP" && to_which=="INR")
        {
            return Main_unit*102;
        }
        else if(Conv_unit=="INR" && to_which=="GBP")
        {
            return Main_unit/102;
        }
        else
        {
            return -1;
        }
    }
};
int main()
{
    string input1,input2,input3,input4;
    UnitConverter unit1(200,"cm"),unit2(40,"kg"),unit3(100,"C"),unit4(50,"USD");
    cout<<"Convert 200 cm to? ";
    cin>>input1;
    cout<<unit1.Length(input1);
    cout<<endl;
    cout<<"Convert 40 kg to? ";
    cin>>input2;
    cout<<unit2.Weight(input2);
    cout<<endl;
    cout<<"Convert 100 C to? ";
    cin>>input3;
    cout<<unit3.Temperature(input3);
    cout<<endl;
    cout<<"Convert 50 USD to? ";
    cin>>input4;
    cout<<unit4.Currency(input4);
    cout<<endl;

    return 0;
}