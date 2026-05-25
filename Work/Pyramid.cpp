#include <iostream>
#include <cstdlib>

using namespace std;

// Normal pyramid
void pyramid(string n, string sum, int rows){
    for(int i = 0; i < rows; i++){
        for(int j = i; j < rows; j++){
            cout << " ";
        }
        cout << sum << endl;
        (sum += n + n);
    }
    cout << "Number of rows: " << rows << endl;
    cout << "Number of asterisks in the longest row: " << (rows * 2) - 1 << endl;
    cout << "Number of total asterisks: " << (rows * rows) << endl;
}

int main(){

    string sum = "^";
    int rows;
    cout << "Enter number of rows: ";
    cin >> rows;
    cin.get();
    pyramid(sum, sum, rows);

    // Alternative / Advance method
    /*int rows;
    int p = 0;
    cout << "Enter number of rows: ";
    cin >> rows;
    for(int i = 0; i < rows; i++){
        for(int j = i; j < rows; j++){
            cout << " ";
        }
        for(int k = 0; k <= p; k++){
            cout << "*";
        }
        p = p + 2;
        // p +=2;
        cout << endl;
    }
    cout << "Number of rows: " << rows << endl;
    cout << "Number of asterisks in the longest row: " << (rows * 2) - 1 << endl;
    cout << "Number of total asterisks: " << (rows * rows) << endl;
    */
    
    return 0;
}