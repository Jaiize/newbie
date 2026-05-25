#include <iostream>
#include <queue>

using namespace std;

int main(){

    // Uses the push back feature of deque
    // queue <int, deque<int>>(man);
    queue <int, deque<int>> man;
    man.push(5);
    man.push(4);
    man.push(3);
    man.push(2);


    cout << "Queue: ";
    while(!man.empty()){
      cout << man.front() << " ";
      man.pop();
    }
    cout << '\n';

    //priority_queue <int, vector <int>> nums;
    // priority_queue <int>(nums);
    priority_queue <int> nums;
    nums.push(5);
    nums.push(10);
    nums.push(9);
    nums.push(2);

    cout << "Priority queue: ";
    while(!nums.empty()){
      cout << nums.top() << " ";
      nums.pop();
    }
    cout << '\n';


    // NB: when altering order vector<int> must be defined / used
    // priority_queue <int, vector<int>, greater<int>>(yeh);
    priority_queue <int, vector<int>, greater<int>> yeh;
    yeh.push(10);
    yeh.push(15);
    yeh.push(9);
    yeh.push(3);

    cout << "Priority Queue advanced testing: " ;
    while(!yeh.empty()){
        cout << yeh.top() << " ";
        yeh.pop();
    }
    cout << '\n';
    

  return 0;
}