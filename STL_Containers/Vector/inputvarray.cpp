#include <iostream>
#include <vector>

using namespace std;

int main(){
    int nums;
    vector <int> more;
    // Same method also works for string

    cout << "Enter a list of numbers to be displayed in sorted order followed by \"0\" to quit the program!" << endl;

    while(cin >> nums){
        if(nums == 0){
            break;
        }
        more.push_back(nums);
    }
    
    int n = more.size();

    // Sorting
    int temp;

    /*for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(more[i] > more[j]){
                temp = more[i];
                more[i] = more[j];
                more[j] = temp;
            }
        }
    }*/
    int j;
    for(int i = 1; (i <= n - 1); i++){
        temp = more[i];
        j = i - 1;
        while((temp < more[j]) && (j>=0)){
            more[j + 1] = more[j];
            j = j - 1;
        }
        more[j + 1] = temp;
    }

    cout << "Sorted input: ";
    /*
    // print stl containers with iterator while loop
    vector <int> :: iterator itr = more.begin();
    while(itr != more.end()){
        cout << *itr << " ";
        itr++;
    }
    */
    vector <int> :: iterator itr;
    for(itr = more.begin(); itr != more.end(); itr++){
        cout << *itr << " ";
    }

    
    return 0;
}