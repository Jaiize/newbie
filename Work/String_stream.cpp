#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){

    int man = 50;

    cout << "Man (int) variable is converted to a string data: " << to_string(man) << endl;

    int num = 20;
    string check;
    stringstream hay;
    hay << num;
    check = hay.str();

    // Another method (works on string to int too)
    // hay << num;
    // hay >> check;

    cout << "Num (int) variable is converted to a string data: " << check << endl;

    int p;
    string you = "30";
    stringstream ss;
    ss << you;
    ss >> p;
    cout << "String to int: " << p + 1 << endl;

    // int k = 44;
    // string strin;
    // ostringstream os;
    // os << k;
    // strin = os.str();
    //cout << strin << endl;

    istringstream is;
    
    
    


    

    return 0;
}
