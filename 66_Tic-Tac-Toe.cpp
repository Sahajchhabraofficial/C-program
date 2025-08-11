//TIC-TAC-TOE GAME!
#include<iostream>
using namespace std;
void singlePlayer()
{
    char t;
    cout<<" ________ "<<endl;
    cout<<"| O or X |"<<endl;
    cout<<"----------"<<endl;
    cout<<"    ";
    cin>>t;
    if(t=='o' || t=='O')
    {
        int choice;
        cout<<"_---+---+---_"<<endl;
        cout<<"|   |   |   |"<<endl;
        cout<<"|   |   |   |"<<endl;
        cout<<"|   |   |   |"<<endl;
        cout<<"*---+---+---*"<<endl;
        start:
        cout<<"enter position:";
        cin>>choice;
        switch(choice)
        {
            case 1: cout<<"_---+---+---_"<<endl;
                    cout<<"| O |   | X |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 2: cout<<"_---+---+---_"<<endl;
                    cout<<"|   | O |   |"<<endl;
                    cout<<"|   | X |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 3: cout<<"_---+---+---_"<<endl;
                    cout<<"| X |   | O |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 4: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"| O |   |   |"<<endl;
                    cout<<"|   |   | X |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 5: cout<<"_---+---+---_"<<endl;
                    cout<<"|   | X |   |"<<endl;
                    cout<<"|   | O |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 6: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   | O |"<<endl;
                    cout<<"|   | X |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 7: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   | X |   |"<<endl;
                    cout<<"| O |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 8: cout<<"_---+---+---_"<<endl;
                    cout<<"| X |   |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   | O |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 9: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   | X |"<<endl;
                    cout<<"|   |   | O |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            default: cout<<"you have enter invalid value!"<<endl;
                    goto start;
        }
    }
    else{
        int choice;
        cout<<"_---+---+---_"<<endl;
        cout<<"|   |   |   |"<<endl;
        cout<<"|   |   |   |"<<endl;
        cout<<"|   |   |   |"<<endl;
        cout<<"*---+---+---*"<<endl;
        elsestart:
        cout<<"enter position:";
        cin>>choice;
        switch(choice)
        {
            case 1: cout<<"_---+---+---_"<<endl;
                    cout<<"| X |   | O |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 2: cout<<"_---+---+---_"<<endl;
                    cout<<"|   | X |   |"<<endl;
                    cout<<"|   | O |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 3: cout<<"_---+---+---_"<<endl;
                    cout<<"| O |   | X |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 4: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"| X |   |   |"<<endl;
                    cout<<"|   |   | O |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 5: cout<<"_---+---+---_"<<endl;
                    cout<<"|   | O |   |"<<endl;
                    cout<<"|   | X |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 6: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   | X |"<<endl;
                    cout<<"|   | O |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 7: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   | O |   |"<<endl;
                    cout<<"| X |   |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 8: cout<<"_---+---+---_"<<endl;
                    cout<<"| O |   |   |"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   | X |   |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            case 9: cout<<"_---+---+---_"<<endl;
                    cout<<"|   |   |   |"<<endl;
                    cout<<"|   |   | O |"<<endl;
                    cout<<"|   |   | X |"<<endl;
                    cout<<"*---+---+---*"<<endl;break;
            default: cout<<"you have enter invalid value!"<<endl;
                    goto elsestart;
        }
    }
}    
void Multiplayer()
{
    char t;
    cout<<" ________ "<<endl;
    cout<<"| O or X |"<<endl;
    cout<<"----------"<<endl;
    cout<<"    ";
    cin>>t;
}
int main()
{
    string playMode;
    cout<<"=========TIC-TAC-TOE======"<<endl;
    cout<<"||      *singleplayer*     ||"<<endl;
    cout<<"||      *multiplayer*      ||"<<endl;
    cout<<"-->>";
    cin>>playMode;
    
    if(playMode=="singleplayer")
    {
        singlePlayer();
    }
    else{
        Multiplayer();
    }

    return 0;
}