#include <iostream>
#include <cstdlib>


using namespace std;    
    

int main(){

    // Printing Left-angle asterisk
    int row;
    cout << "Enter number of Left-angle asterisk to display: ";
    cin >> row;

    cout << endl;

    int a = (row * 2) - 1;
    int p = 0;

    // Normal
    for(int i = 0; i < row; i++){
        for(int j = 0; j < a; j++){
            cout << " ";
        }
        a -= 2;

        for(int k = 0; k <= p; k++){
            cout << "*";
        }
        cout << endl;
        p += 2;
    }
    cout << endl;
    
    // Upside down
    int b = 0;
    int c = (row * 2) - 1;
    for(int i = 0; i < row; i++){
        for(int j = 0; j <= b; j++){
            cout << " ";
        }
        b += 2;

        for(int k = 0; k < c; k++){
            cout << "*";
        }
        cout << endl;
        c -= 2;
    }
    cout << endl;

    // Scanty Left-angle asterisk
    int e = (row * 2) - 1;
    int f = 0;
    for(int i = 0; i < row; i++){
        for(int j = 0; j < e; j++){
            cout << " ";
        }
        e -= 2;
        if(i == 0){
            cout << "*" << endl;
        }

        if(i > 0 && i != row - 1){
            cout << "*";
            for(int j = 0; j <= f; j++){
                cout << " ";
            }
            cout << "*";
            cout << endl;
            f += 2;
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
    
    // Upside-down Scanty Left-angle asterisk
    int g = 0;
    int h = (row - 2) * 2 - 1; // or (row * 2) - 5
    for(int i = 0; i < row; i++){
        for(int j = 0; j <= g; j++){
            cout << " ";
        }
        g += 2;
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
            for(int j = 0; j < h; j++){
                cout << " ";
            }
            cout << "*";
            cout << endl;
            h -= 2;
        }
        if(i == row - 1 && i != 0){
            cout << "*" << endl;
        }

    }


    return 0;
}