//wap that classify different sets.
#include<iostream>
using namespace std;
class Sets
{
    int arr[5];
    int brr[5];
    int temp[5];
public:
    Sets(){}
    Sets(int a0, int a1, int a2, int a3, int a4)
    {
        arr[0] = a0;
        arr[1] = a1;
        arr[2] = a2;
        arr[3] = a3;
        arr[4] = a4;
    }
    Sets operator-(Sets obj)
    {
        Sets result;
        int k = 0;
        for(int i=0; i<5; i++)
        {
            bool found = false;
            for(int j=0; j<5; j++)
            {
                if(arr[i] == obj.arr[j])
                {
                    found = true;
                    break;
                }
            }
            if(!found && k < 5)
            {
                result.arr[k++] = arr[i];
            }
        }
        // Fill remaining elements with 0 for clarity
        for(int i = k; i < 5; i++) {
            result.arr[i] = 0;
        }
        return result;
    }
    friend ostream& operator<<(ostream& os, const Sets& s);
};

ostream& operator<<(ostream& os, const Sets& s)
{
    os << "{ ";
    for(int i = 0; i < 5; i++)
    {
        if (s.arr[i] != 0)
            os << s.arr[i] << " ";
    }
    os << "}";
    return os;
}
int main()
{
    Sets s1(10,20,30,40,50),s2(20,40,60,80,100),s3;
    s3 = s1 - s2;
    cout<<s3;

    return 0;
}