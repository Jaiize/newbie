#include <iostream>
#include <set>
#include <unordered_set>

using namespace std;

int main(){
  
  // greater<int> | prints array in descending order
  // greater_equal<int> | prints array in descending order and includes duplicate element
  // less<int> | prints array in ascending order
  // less_equal<int> | prints array in ascending order with duplicate element


  set <int> man = {4, 5, 6, 8, 5, 2, 1};
  // man.erase(man.begin()); // Removes first element -> 1 since it's an ordered set
  // Only on associative STL Containers
  auto ub = man.upper_bound(5); // (>) greater than the number in the parenthesis
  auto lb = man.lower_bound(2); // (>=) greater than or equals to the number in the parenthesis
  cout << *ub << '\n' << *lb << endl;

  cout << "set: ";
  for(auto i = man.begin(); i != man.end(); ++i){
    cout << *i << " ";
  }
  cout << endl;

  unordered_set <int> nums = {4, 5, 6, 8, 5};
  nums.insert({1, 2});
  cout << "Unordered set: ";
  for(auto i = nums.begin(); i != nums.end(); ++i){
    cout << *i << " ";
  }
  cout << endl;

  
  multiset <int> hay = {4, 5, 8, 5, 7};
  hay.insert(hay.begin(), 1);

  cout << "Multiset: ";
  for(const auto & i: hay){
    cout << i << " ";
  }
  cout << '\n';
  

  cout << "Unordered multiset: ";
  unordered_multiset <int> num = {4, 5, 8, 5, 7};
  
  for(auto& i: num){
    cout << i << " ";
  }
  cout << '\n';


  
  return 0;
}