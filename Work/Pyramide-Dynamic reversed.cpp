#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
   
    int row;
    cout << "Enter number of dynamic-pyramid asterisk to display: ";
    cin >> row;
    int p = (row - 2) * 2 - 1;
    // int p = (row * 2) - 5 // Simpler formula;   


    for(int i = 0; i < row; i++){
        for(int j = 0; j <= i; j++){
            cout << " ";
        }
        if(i == 0){
            cout << "*";
            for(int i = 0; i < row - 1; i++){
                // cout << " *";
                cout << " ";
                cout << "*";
            }
            cout << endl;
        }
        if(i > 0 && i != row - 1){
            cout << "*";
            for(int i = 0; i < p; i++){
                cout << " ";
            }
            cout << "*";
            p -= 2;
            cout << endl;
        }
        if(i == row - 1 && i != 0){
            cout << "*";
        }
        
    }

    cout << "\n";

    return 0;
}