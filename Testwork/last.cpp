#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
// #include <math.h>
#include <numeric>


using namespace std;

int forMax(int one, int sec){
    return (one > sec) ? one : sec;
}

void tester(int test[3][3], int rol, int col){
    for(int i = 0; i < rol; i++){
        cout << "|";
        for(int j = 0; j < col; j++){
            cout << test[i][j];
            if(j == 0 || j == 1){
                cout << ", ";
            }
        }
        cout << "|";
        cout << endl;
    }
    /*if(tes.compare(test) == false){
        cout << "Yes!" << endl;
    }else{
        cout << "No!" << endl;
    }
    cout << endl;

    for(auto i: test){
        // cout << i ;
    }*/

}


void work(int nums[], int n){
    int sum = 0;
    int max = 0;
    for(int i = 0; i < n; i++){
       sum = forMax(nums[i], sum + nums[i]);
       max = forMax(sum, max);
    }
    cout << "Sum: " << sum << "\nMax: " << max << endl;
    
}


// void Solution(vector<vector<string>> queries){
vector<string>Solution(vector<vector<string>> queries){
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
                    queries[i - 3][j - 1] = "\"\"";
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
    return master;

}


int main(){

    vector<vector<string>> mass_Queries = {{"SET", "0", "A", "B", "4"}, {"SET", "1", "A", "C", "6"}, {"COMPARE_AND_SET", "2", "A", "B", "4", "9"}, 
    {"COMPARE_AND_SET", "3", "A", "C", "4", "9"}, {"COMPARE_AND_DELETE", "4", "A", "C", "6"}, {"GET", "5", "A", "C"}, {"GET", "6", "A", "B"}};

    // int nums[] = {0, 0, 1, 0, 1, 1, 0, 1, 0, 0 };
    // int nums[] = {3, 0, 8, 2, 1, 5, 9};
    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int s = sizeof(nums) / sizeof(nums[0]);
    int numbers[3][2] = {{7, 2}, {4, 8}, {2, 3}};


    int no[3][3] = {{4, 2, 0}, {1, 7, 9}, {8, 5, 3}};
    int rol = sizeof(no) / sizeof(no[0]);
    int col = sizeof(no[0]) / sizeof(no[0][0]);
    // Solution(mass_Queries);
    // tester(no, rol, col);
    // work(nums, s);

    vector<string> getter = Solution(mass_Queries);

    cout << "[";
    for(int i = 0; i < getter.size(); i++){
        if(i == getter.size() - 1){
            cout << getter[i];
            continue;
        }
        cout << getter[i] << " ";
    }
    cout << "]";


    

    return 0;
}
