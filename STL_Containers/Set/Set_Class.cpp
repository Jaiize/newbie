#include <iostream>
#include <set>

using namespace std;

class Man{
    public:
        int age;
        float money;
        string name;
        void printInfo() const {
            cout << age << " " << name << " - " << money << endl;
        }
    bool operator > (const Man& check) const {
        return ((*this).age > check.age);
    }


};


int main(){

    multiset <Man, greater<>> mset = {{20, 1500.12, "Edward"}, {45, 2000.11, "lex"}, {25, 4000.145, "Jude"}};

    for(const auto& i: mset){
        i.printInfo();
    }

    /*for(const auto& i: mset){
        cout << i.age << " " << i.money << " - " << i.name << endl;
    }*/




    return 0;
}