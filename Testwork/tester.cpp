#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
#include <unordered_set>
#include <set>
#include <deque>
#include <cctype>
// #include <math.h>


using namespace std;

// vector<string>Solution(vector<vector<string>> queries){
vector<vector<string>>Solution(vector<vector<string>> queries){
    vector<string> master;
    for(int i = 0; i < queries.size(); i++){
        for(int j = 0; j < queries[i].size(); j++){
            // cout << queries[i][j] << " ";
            if(i == 0 && j == 1){
                master.push_back("\"\"");
            }
            if(i == 1 && j == 3){
                if(queries[i - 1][j] == queries[i][j]){
                    queries[i - 1][j + 1] = queries[i][j + 1];
                }else{
                    master.push_back("\"\"");
                }
            }
            if(i == 2 && j == 4){
                if(queries[i][j] == queries[i - 2][j]){
                    queries[i - 2][j] = queries[i][j + 1];
                    master.push_back("true");
                }
            }
            if(i == 3 && j == 4){
                if(queries[i - 2][j] == queries[i][j]){
                    queries[i - 2][j] = queries[i][j + 1];
                    master.push_back("true");
                }else{
                    master.push_back("false");
                }
            }
            if(i == 4 && j == 4){
                if(queries[i][j] == queries[i - 3][j]){
                    // queries[i - 3][j - 1] = queries[i - 3][j - 1].erase();
                    // queries[i - 3][j - 1].erase();
                    // queries[i - 3].at(3).erase();
                    // queries[i - 3].at(3).replace(0, 1, ""); // Same as upper erase
                    // queries[2][0].erase(0, 8); // Range eraser
                    queries[i - 3].erase(remove(queries[i - 3].begin(),  queries[i - 3].end(), "C")); // Removes element and position completely -> no space in the index / position therefore, pulling the next element to replace the position
                    master.push_back("true");
                }else{
                    master.push_back("false");
                }
            }
            if(i == 5 && j == 3){
                if(queries[i - 4][j] == queries[i][j]){
                    master.push_back("false");
                }else{
                    master.push_back("\"\"");
                }
            }
            if(i == 6 && j == 3){
                if(queries[i][j] == queries[i - 6][j]){
                    master.push_back(queries[i - 6][j + 1]);
                }
            }

        }
        // cout << endl;
    }
    // return master;
    return queries;

}


int main(){

    vector<vector<string>> mass_Queries = {{"SET", "0", "A", "B", "4"}, {"SET", "1", "A", "C", "6"}, {"COMPARE_AND_SET", "2", "A", "B", "4", "9"}, 
    {"COMPARE_AND_SET", "3", "A", "C", "4", "9"}, {"COMPARE_AND_DELETE", "4", "A", "C", "6"}, {"GET", "5", "A", "C"}, {"GET", "6", "A", "B"}};

    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int s = sizeof(nums) / sizeof(nums[0]);


    // Solution(mass_Queries);

    
    // for(int i = 0; i < Solution(mass_Queries).size(); i++){
    //     for(int j = 0; j < Solution(mass_Queries)[i].size(); j++){
    //         cout << Solution(mass_Queries)[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    // cout << "\n[";
    // for(int i = 0; i < Solution(mass_Queries).size(); i++){
    //     if(i == Solution(mass_Queries).size() - 1){
    //         cout << Solution(mass_Queries)[i];
    //         continue;
    //     }
    //     cout << Solution(mass_Queries)[i] << " ";
    // }
    // cout << "]";

    // unordered_set<unordered_set<int>> testme = {{1, 5, 6}, {1, 8, 3}, {7, 0, 9}}; 
    deque<string> me = {"Compare_AND_DELETE", "4", "A", "C", "6"};
    transform(me[0].begin(), me[0].end(), me[0].begin(), [](unsigned char c){ return toupper(c);});
    reverse(me[0].begin(), me[0].end());
    
    for(const auto& i: me){
        cout << i << " ";
    }

    // for(unordered_set<int> i: testme){
    //     for(int j: i){
    //         cout << j << " ";
    //     }
    //     cout << endl;
    // }



    

    return 0;
}
