#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>

using namespace std;

int main(){

    // Removing duplicate elements from an array
    vector<int> test = {1, 5, 6, 1, 8, 3, 7, 5, 9};
    // Method one
    cout << "Before: ";
    for(const auto& i: test){
        cout << i << " ";
    }
    cout << endl;

    set<int> one(test.begin(), test.end());
    test.assign(one.begin(), one.end());   

    cout << "After: ";
    for(const auto& i: test){
        cout << i << " ";
    }
    cout << endl;

    vector<int> no = {2, 4, 6, 2, 8, 3, 7, 4, 9};
    // Method two
    cout << "Before: ";
    for(const auto& i: no){
        cout << i << " ";
    }
    cout << endl;
    unordered_set<int> two; // Normal set will work too
    for(const auto& i: no){
        two.insert(i);
    }

    no.assign(two.begin(), two.end());
    cout << "After: ";
    for(const auto& i: no){
        cout << i << " ";
    }
    cout << endl;  
    
    
    string sentence = ("The boy just got here!");
    string boy = "Edward Jordan";
    set <char> box;
    for(int i = 0; i < boy.length(); ++i){
        char show = boy.at(i);
        // box.insert(boy.at(i));
        box.insert(show);
    } 

    for(int j = 0; j < sentence.length(); ++j){
        char text = sentence.at(j);
        box.erase(text);
    }

    if(box.empty() == false){
        cout << "All elements were not present, hence the element(s) left!" << endl;
        for(const auto & i: box){
            cout << i << " ";
        }

    }else{
        cout << "All elements were present and deleted!" << endl;
    }

    return 0;
}