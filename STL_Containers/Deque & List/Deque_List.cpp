#include <iostream>
#include <deque>
#include <list>
#include <forward_list>

using namespace std;

int main(){
    deque<int> nums = {4, 5, 8, 5};
    nums.insert(nums.begin() + 2, 1); // 4 5 1 8 5 // Does not work on list & forward_list class
    nums.push_back(9);
    nums.push_front(9);
    nums.pop_back();
    nums.pop_front();
    // nums.erase(nums.begin()) // Removes the first element
    // nums.front(); // Available on vector too
    // nums.back();
    cout << "Deque: ";
    for (auto i = nums.begin(); i != nums.end(); ++i)
    {
        cout << *i << " ";
    }
    cout << '\n';

    list<int> man = {5, 6, 5, 2, 3};
    man.insert(man.begin(), 1); // 1 5 6 5 2 3
    man.push_back(9);
    // man.erase(man.begin()); // Removes the first element
    // man.reverse();  // backward display
    // man.push_front(9);
    cout << "List: ";
    for (auto i : man)
    {
        cout << i << " ";
    }
    cout << '\n';

    forward_list<int> jude = {4, 5, 8, 5};
    jude.insert_after(jude.begin(), 1);
    jude.push_front(9);
    jude.push_front(9);
    jude.pop_front();
    jude.emplace_after(jude.begin(), 12);
    jude.emplace_front(0);
    // jude.erase_after(jude.begin()); // Removes the second element

    cout << "Forward List: ";
    for (auto &i : jude)
    {
        cout << i << " ";
    }
    cout << '\n';

    return 0;
}