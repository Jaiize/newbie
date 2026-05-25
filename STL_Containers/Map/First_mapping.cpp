#include <iostream>
#include <map>
#include <unordered_map>

using namespace std;

int main(){

    // greater<int> | prints array in descending order
    // greater_equal<int> | prints array in descending order and includes duplicate key
    // less<int> | prints array in ascending order
    // less_equal<int> | prints array in ascending order with duplicate key
    
    map <char, int> man = {{'T', 10}, {'S', 54}};
    man['O'] = 88;
    man.insert(pair <char, int>('D', 99)); //or{'D', 99}
    pair <char, int> c1('K', 78); //or {'K', 78}
    man.insert(c1);
    man.insert(make_pair('E', 40));

    cout << man['E'] << endl;
    //man.erase(c1.first); man.erase('K') | man.clear()
    cout << c1.first  << endl;
    cout << c1.second << endl;

    cout << "The size of the map is: " << man.size() << '\n';

    if(man.empty() == false){
        cout << "The map is not empty!" << endl;
    }else{
        cout << "The map is empty" << endl;
    }
    cout << man.empty() << endl;
    map <char, int> :: iterator iter;
    for(iter = man.begin(); iter != man.end(); ++iter){
        cout << (*iter).first << " ";
        cout << iter->second << " ";
    }
    cout << '\n';

    // bucket.size() & bucket.count | only work on unordered associative containers
    // count() | works on associative & Unordered assosciative containers
    
    string show = "Joseph the tycoon man";
    unordered_map <char, int> check;
    for(int i = 0; i < show.length(); i++){
        char texts = show[i];
       if(check.find(texts) != check.end()){
            check[texts]++;
       }else{
        check[texts] = 1;
       }
        
        cout << "(";
        cout << texts << " = " << check[texts] << ") \n";
    }
    cout << "\n";
    for(auto itr = check.begin(); itr != check.end(); itr++){
        cout << itr->first << ": " << (*itr).second << endl;
    }
    cout << endl;
    /*
    Another way of displaying map elements
    for(const auto& i: check)
    or
    for(auto& i: check){
        cout << i.first << " - " << i.second <<endl;
    }
    Also how to print key enquiry with iterator
    auto itr = man.find('T');
    cout << itr->first << " " << (*itr).second << endl;
    
*/

    return 0;
}