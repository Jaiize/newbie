#include <iostream>
#include <stack>

using namespace std;

int main(){
    
    // Uses the push front feature of deque
    // stack <int, deque<int>>(nums);
    stack <int, deque<int>> nums;
    nums.push(4);
    nums.push(10);
    nums.push(9);
    nums.push(1);
    cout << "Stack: ";
    while (!nums.empty()){
        cout << nums.top() << " ";
        nums.pop();
    }
    



    return 0;
}