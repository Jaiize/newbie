#include <iostream>
#include <cstdlib>

using namespace std;

#ifndef PERSON_H
#define PERSON_H
class Person {
    public:
        Person(string fn, string sn);
        const string& getFirstName() const;
        const string& getSecondName() const;
        friend ostream& operator << (ostream& out, Person& p);  
    private:
        const string& first_name;
        const string& second_name;
};
#endif

Person::Person(string fn, string sn): first_name(fn), second_name(sn){
}

const string& Person::getFirstName() const {
    return first_name;
}

const string& Person::getSecondName() const {
    return second_name;
}

ostream& operator << (ostream& out, Person& p){
    out << "first_name = " << p.getFirstName() << " "
    << "second_name = " << p.getSecondName() << " ";
    return out;

}

int main(){

    string first_name, second_name, event;
    cout << "Enter the \"first\", \"second\" name and event" << endl;
    cin >> first_name >> second_name >> event;

    // Person p(first_name, second_name);
    auto p = Person(first_name, second_name);
    cout << p << "Event = " << event; // confirm the spacing for perfection
    
    cout << "\n";
    system("pause");
    return 0;
}


