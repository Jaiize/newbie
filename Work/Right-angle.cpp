#include <iostream>
#include <cstdlib>


using namespace std;    
    

int main(){

    // Printing Right-angle asterisk
    int row;
    cout << "Enter number of Right-angle asterisk to display: ";
    cin >> row;

    cout << endl;

    int p = 0;

    // Normal
    for(int i = 0; i < row; i++){
        for(int k = 0; k <= p; k++){
            cout << "*";
        }
        cout << endl;
        p += 2;
    }
    cout << endl;
    // Upside down
    int a = (row * 2) - 1;
    for(int i = 0; i < row; i++){
        for(int k = 0; k < a; k++){
            cout << "*";
        }
        cout << endl;
        a -= 2;
    }
    cout << endl;

    // Scanty Right-angle asterisk
    int c = 0;
    for(int i = 0; i < row; i++){
        if(i == 0){
            cout << "*" << endl;
            // continue;
        }
        if(i > 0 && i != row - 1){
            cout << "*";
            for(int j = 0; j <= c; j++){
                cout << " ";
            }
            cout << "*";
            cout << endl;
            c += 2;
        }
        if(i == row - 1 && i != 0){
            cout << "*";
            for(int k = 0; k < row - 1; k++){
                cout << " ";
                cout << "*";
            }
        }
    }
    cout << endl;

    // Upside-down Scanty Right-angle asterisk
    int r = (row - 2) * 2 - 1; // Or (row * 2) - 5;

    for(int i = 0; i < row; i++){
        if(i == 0){
            cout << "*";
            for(int k = 0; k < row - 1; k++){
                cout << " ";
                cout << "*";
            }
            cout << endl;
        }
        if(i > 0 && i != row - 1){
            cout << "*";
            for(int j = 0; j < r; j++){
                cout << " ";
            }
            cout << "*";
            cout << endl;
            r -= 2;
        }
        if(i == row - 1 && i != 0){
            cout << "*" << endl;
        }
    }
    cout << endl;
    

    return 0;
}