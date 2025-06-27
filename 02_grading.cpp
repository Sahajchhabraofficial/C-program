//wwap to check if a student got passed in exam or not.
#include<iostream>
using namespace std;
int main()
{
  int hin, eng, math, sci,ai,per;
  cout<<"enter your hindi marks: ";
  cin>>hin;
  cout<<"enter your english marks: ";
  cin>>eng;
  cout<<"enter your math marks: ";
  cin>>math;
  cout<<"enter your science marks: ";
  cin>>sci;
  cout<<"enter your ai marks: ";
  cin>>ai;
  per=hin+eng+math+sci+ai/500*100;
  if(per>33)
  {
    cout<<"you got passed in exam";
  }
  else{
    cout<<"you have failed in this exam";
  }
  
}