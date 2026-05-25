#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void check(vector <int> nums){
    // nums.erase(nums.begin()); // Removes the first element -> 4
    cout << "Unsorted Array: ";
    for(int k: nums){
        cout << k << " ";
    }
    cout << endl;
    
    //Sort
    int n = nums.size();
    int temp;
    int j;
    for(int i = 1; i <= n - 1; i++){
        temp = nums[i];
        j = i - 1;
        while((temp < nums[j]) && (j>=0)){
            nums[j + 1] = nums[j];
            j = j - 1;
        }
        nums[j + 1] = temp;
    }/*
    //Another method
    int temp;
    for(int i = 0; i < n; ++i){
        for(int j = i + 1; j < n; ++j){
            if(nums[j] < nums[i]){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;

            }
        }
    }
    */
    //print
    cout << "Sorted Array: ";
    /*
    // printing stl containers with iterator while loop
    vector <int> :: iterator itr = nums.begin();
    while(itr != nums.end()){
        cout << *itr << " ";
        itr++;
    }
    */
    for(const int & j: nums){
        cout << j << " ";
    }
    cout <<'\n';
    cout << "Solution: ";
    
    for(int i = 0; i < n; i++){
        if(nums[i] % 2 == 0){
            cout << nums[i] << " ";
        }
    }
    // cout << nums.front() << ", " << nums.back() << endl;


}
int main(){

    vector<vector<int>> testme = {{4, 5, 6}, {1, 2, 3}, {7, 8, 95}};
    testme[1].erase(remove(testme[1].begin(), testme[1].end(), 2)); // removes element testme[1][1] -> 
    
    vector <int> man = {4, 8, 2, 9, 1, 7};
    man.erase(man.begin() + 2, man.end() - 1); // 4 8 7
    //vector <int> hey = {0, 4, 7, 1, 8, 2};
    //man.swap(hey);
    //man.insert(man.begin() + 5, 5);
    man.front(); // Prints the first element in the array
    man.back(); // Prints the last element in the array
    //man.shrink_to_fit();
    //cout << man.size() << endl;
    //cout << man.capacity() << endl;
    //cout << man.max_size() << endl;
    check(man); 
    vector<int> :: iterator itr;
    for(itr = man.begin(); itr != man.end(); itr++){
        // if(itr == man.begin()){
        //     continue;
        // }
        cout << *itr << " ";
    }



    return 0;
}