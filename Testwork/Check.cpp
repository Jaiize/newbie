#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <cmath>
// #include <math.h>


using namespace std;

int forMax(int one, int sec){
    return (one > sec) ? one : sec;
}

#ifndef CABIN_H
#define CABIN_H

class Cabin{
    public:
        Cabin(vector<int> arr);
        void solution();
    private:
        vector<int> nums;
};
#endif


int tester(int test[], int s){
    int sum = 0;
    int max = 0;
    for(int i = 0; i < s; i++){
        sum += test[i];
        if(test[i] > sum){
            sum = test[i];
        }else if(sum > test[i]){
            sum = sum;
        }
        
        if(sum > max){
            max = sum;
        }else if(max > sum){
            max = max;
        }

    }
    return max;

}


int main(){

    // int nums[] = {3, 4, -7, 3, 1, 3, 1, -4, -2, -2};
    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int s = sizeof(nums) / sizeof(nums[0]);


    vector<int> numbers = {2, 5, 1, 4, 8};
    numbers.insert(numbers.begin() + 1, {45, 12});
    int ss = numbers.size();

    // cout << tester(nums, s);


    // Cabin cab(numbers);
    // cab.solution();
    // int jake{4};
    // cout << jake;
    
    



#if 0
    LABEL:

    int rows;
    cout << "Enter number of Dynamic-pyramid asterisk to display: ";
    cin >> rows;

    cout << endl;
    int a = (rows * 2) - 1;
    int aa = 0;
    int p = 0;
    // int d = (rows * 2) - 1;
    int q = (rows - 2) * 2 - 1; // int q = (rows * 2) - 5;

    // Normal scanty
    for(int i = 0; i < rows; i++){
        for(int j = i; j < rows; j++){
            cout << " ";
        }
        if(i == 0){
            cout << "*";
            cout << endl;
        }
        if(i > 0 && i != rows - 1){
            cout << "*";
            for(int l = 0; l <= p; l++){
                cout << " ";
            }
            cout << "*" << endl;
            p += 2;

        }
        if(i == rows - 1 && i != 0){
            cout << "*";
            for(int i = 0; i < rows - 1; i++){
                // cout << " *";
                cout << " ";
                cout << "*";
            }
            cout << endl;
        }

    }

    // Upside Down
    for(int i = 0; i < rows; i++){
        for(int j = 0; j <= i; j++){
            cout << " ";
        }
        if(i == 0){
            cout << "*";
            for(int i = 0; i < rows - 1; i++){
                // cout << " *";
                cout << " ";
                cout << "*";
            }
            cout << endl;
        }
        if(i > 0 && i != rows - 1){
            cout << "*";
            for(int i = 0; i < q; i++){
                cout << " ";
            }
            cout << "*";
            q -= 2;
            cout << endl;
        }
        if(i == rows - 1 && i != 0){
            cout << "*";
        }
    }



    cout << "\n";
    goto LABEL;

#endif

    float ceel = 19.569;
    // int ceel = 1905;
    // cout << ceel << " = " << setprecision(2) << fixed << ceel << endl;
    // cout << ceel << " = " << setprecision(0) << ceel << endl; // Use '0' only after using "fixed" at first
    // cout << ceel << " = " << setprecision(2) << ceel << endl;
    cout << ceel << " = " << roundf(ceel) << endl;
    // cout << ceel << " = " << truncf(ceel) << endl; // 13.56 = 13
    // MinGW download map: dev, gccg++, gccobjc or any compiler description

    return 0;
}
