#include <iostream>
#include <algorithm>

using namespace std;

struct Jaize{
    //public:
    Jaize(int arr[], int n);
    void merge(int X[], int Y[], int m, int n);
    void printArray(int arr[], int n);

};

Jaize::Jaize(int arr[], int n){

    int temp;
    int j;
    for(int i = 1; (i <= n - 1); i++){
        temp = arr[i];
        j = i - 1;
        while((temp < arr[j]) && (j>=0)){
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = temp;
    }


}

void Jaize::merge(int X[], int Y[], int m, int n){

    for(int i = 0; i < m; i++){
        if(X[i] > Y[0]){
            swap(X[i], Y[0]);
            int first = Y[0];

            int k;
            for(k = 1; k < n && Y[k] < first; k++){
                Y[k - 1] = Y[k];
            }
            Y[k - 1] = first;
        }
    }
}

void Jaize::printArray(int arr[], int n){

    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(){

    /*int X[] = { 1, 8, 10, 4, 7 };
    int Y[] = { 9, 2, 3 };

    int m = sizeof(X) / sizeof(X[0]);
    int n = sizeof(Y) / sizeof(Y[0]);*/

    int X[30];
    int m;
    int Y[30];
    int n;
    cout << "Enter the size of the first array" << endl;
    cin >> m;
    cout << "Enter the first array's contents!" << endl;
    for(int i = 0; i < m; i++){
        cin >> X[i];
    }

    cout << "Enter the size of the second array" << endl;
    cin >> n;
    cout << "Enter the second array's contents!" << endl;
    for(int i = 0; i < n; i++){
        cin >> Y[i];
    }

    Jaize fetch(X, m); 
    Jaize fetch2(Y, n);
    
    fetch.merge(X, Y, m, n);
    cout << "X: ";
    fetch.printArray(X, m);
    cout << "Y: ";
    fetch.printArray(Y, n);
    



    return 0;
}