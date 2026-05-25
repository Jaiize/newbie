#include <iostream>
#include <map>
#include <unordered_map>

using namespace std;

int main(){

    multimap <char, int, greater<int>> nums = {{'A', 10}, {'B', 20}, {'C', 30}};
    nums.insert(make_pair('C', 40));
    nums.insert(pair <char, int>('X', 71));
    nums.insert(pair <char, int>{'X', 74});
    pair <char, int> tosin('G', 87);
    nums.insert(tosin);
    nums.insert(make_pair('C', 30));
    //nums.erase(nums.find('C')); used to erase just one or the first element if multimap(duplicate key)
    /*auto i = nums.erase(nums.find('C')); to erase and print the next available duplicate key 
    cout << i->first << " " << i->second << endl;*/
    cout << "Multimap" << endl;
    for(auto& i: nums){
      cout << i.first << "-" << i.second << endl;
    }

    cout << "C occurrence: " << nums.count('C') << endl;

    /*nums.upper_bound() & nums.lower_bound() work on map & multimap too

    auto ub = nums.upper_bound('C');
    cout << ub->first << " " << ub->second << endl;

    auto lb = nums.lower_bound('C');
    cout << lb->first << " " << lb->second << endl;


    auto itr = nums.equal_range('C');
    for(auto i = itr.first; i != itr.second; ++i){
      cout << i->first << " = " << (*i).second << endl;
    }

    or

    pair <multimap<char, int> :: iterator, multimap <char, int> :: iterator> range =  nums.equal_range('C');
      multimap <char, int> :: iterator k;
      for(k = range.first; k != range.second; ++k){
          cout << k->first << " = " << k->second << endl;
      }

    */
    unordered_multimap <char, int> man = {{'A', 10}, {'B', 20}, {'C', 30}};
    man.insert(make_pair('C', 30));

    cout << "Unordered multimap" << endl;
    for(const auto& i: man){
      cout << i.first << "-" << i.second << endl;
    }
  

    return 0;
}