//FILE HANDLING!
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream doc;
    doc.open("sahaj.txt");
    doc<<"this is the first txt file in the VS code"<<endl;
    doc<<"welcome to the sahaj";
    doc.close();

    return 0;
}