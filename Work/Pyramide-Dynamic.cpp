#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
   
    int row;
    cout << "Enter number of dynamic-pyramid asterisk to display: ";
    cin >> row;
    int p = 1;
    for(int i = 0; i < row; i++){
        for(int j = i; j < row; j++){
            cout << " ";
        }
        
        if(i == 0){
            cout << "*";
            cout << endl;
        }

        if(i > 0 && i != row - 1){
            cout << "*";
            for(int l = 1; l <= p; l++){
                cout << " ";
            }
            cout << "*" << endl;
            p += 2;

        }

        if(i == row - 1 && i != 0){
            cout << "*";
            for(int i = 0; i < row - 1; i++){
                cout << " ";
                cout << "*";
            }
            cout << endl;
        }
        
    }

    cout << "\n";


    return 0;
}