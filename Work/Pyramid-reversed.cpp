#include <iostream>
#include <cstdlib>

using namespace std;

// Reversed pyramid
int main(){
   int rows;
   int p;
   cout << "Enter number of rows: ";
   cin >> rows;
   
   p = (rows * 2) - 1;
   for(int i = 1; i <= rows; i++){
        for(int j = 0; j <= i; j++){
            cout << " ";
        }
        for(int k = 0; k < p; k++){
            cout << "*";
        }
        p = p - 2;
        // p -= 2;
        cout << endl;
    } 
    cout << "Number of rows: " << rows << endl;
    cout << "Number of asterisks in the longest row: " << (rows * 2) - 1 << endl;
    cout << "Number of total asterisks: " << (rows * rows) << endl;

    return 0;
}