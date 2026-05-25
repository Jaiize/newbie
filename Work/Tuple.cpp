#include <iostream>
#include <tuple>

using namespace std;

tuple <char, int> Person(){
  return {'Z', 33};
}

int main(){
  
    tuple <int, string> man (25, "Jordan");
  
    cout << get<0>(man) << ", " << get<1>(man) << endl;
    
    get<0>(man) = 35;
    get<1>(man) = "Joseph";
    
    cout << get<0>(man) << ", " << get<1>(man) << endl;
  
    // Tuple Decomposition = tie();
    tuple <int, char, string> dam;
    dam = make_tuple(40, 'E', "Edward");
  
    int x;
    char y;
    string z;
    tie(x, y, z) = dam;
    cout << x << ", " << y << ", " << z << endl;
    cout << '\n';
  
    // Concatenation = tuple_cat();
    tuple <int, string> cookie = make_tuple(12, "Biscuit");
    tuple <int, string, bool> candy = make_tuple(24, "Sweet", true);
  
    //auto box = tuple_cat(cookie, candy);
    tuple <int, string, int, string, bool> box = tuple_cat(cookie, candy);
    
    int i;
    string j;
    int k;
    string l;
    bool m;
    tie(i, j, k, l, m) = box;
    cout << i << " " << j << " " << k << " " << l << " " << m << endl;
    
    cout << "To string testing: " << to_string(get<0>(cookie)) << endl;
    
  
    // for tuple function
    // tuple <char, int> p = Person();
    // auto [key, age] = Person();
    // cout << key << " - " << age << endl;
    auto p = Person();
    cout << get<0>(p) << " - " << get<1>(p) << endl;
  
  
    return 0;
}