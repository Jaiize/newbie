#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int arrayRange(const int* start, const int* end){

    //const int *pointer = new int;
    
    const int* pointer;
    int result = 0;

    //or for(auto pointer = start; pointer != end pointer++)
    for(pointer = start; pointer != end; pointer++){
        result += *pointer;
        cout << *pointer << " " ;
    }  
    cout << endl;
    cout << "The sum of the selected array is: ";
    return result;
    
    //delete start;
    //delete end;
    //delete pointer;
}

int main(){
    int nums[] = {4, 5, 8, 7, 9, 6, 2};
    int value = arrayRange(nums, nums + 4); // 4 5 8 7
    // int value = arrayRange(nums + 2, nums + 5); // 8 7 9
    cout << value << endl;

    float me = 19.569;
    cout << me << " = " << setprecision(2) << me << endl; // 20 but has to come first before any other setprecisions otherwise "fixed" would trump reslt in that case just set setprecison to "0"
    cout << me << " = " << setprecision(2) << fixed << me << endl; // 19.57 'fixed' maintains the original value, setprecision works on fixed original value
    cout << me << " = " << roundf(me) << endl; // 20
    cout << me << " = " << truncf(me) << endl; // 19
  
   

   
    return 0;
}