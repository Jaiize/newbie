#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    // Removing duplicate elements from an array
    vector<int> test = {1, 5, 6, 1, 8, 3, 7, 5, 9};

    sort(test.begin(), test.end()); // Must be sorted before using unique() otherwise counterfeit 

    test.erase(unique(test.begin(), test.end()), test.end());
   

    for(const auto& i: test){
        cout << i << " ";
    }

    system("pause");
    return 0;
}
