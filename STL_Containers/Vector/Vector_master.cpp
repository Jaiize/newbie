#include <iostream>
#include <vector>

using namespace std;


#ifndef TABLE_H
#define TABLE_H

template <class dim, class sim>
class Table{
    public:
        Table();
        dim addSomeone(vector <sim> someone);
        friend ostream& operator<<(ostream& out, const Table <void, string>& tab);
    private:
        vector <vector<sim>> People;
};
#endif


template <class dim, class sim>
Table <dim, sim>::Table(){
    vector <vector<sim>> People{};
}

template <class dim, class sim>
dim Table <dim, sim>::addSomeone(vector <sim> someone){
    People.push_back(someone);
}


ostream& operator<<(ostream& out, const Table <void, string>& tab){

    for(int i = 0; i < tab.People.size(); i++){
        // for(int j = 0; j < tab.People[i].size(); j++){
        for(int j = 0; j < tab.People[0].size(); j++){
            out <<  tab.People[i][j] << " ";
        }
        out << "\n";
    }

    return out;
    
    /*for(vector<string> h: tab.People){
        for(int i = 0; i < h.size(); i++){
            out << h[i] << " ";
        }
        out << "\n";
    }
    return out;*/

}

int main(){

    Table <void, string> People;
    vector <string> s1 = {"Joseph Tosin", "08066850839"};
    People.addSomeone(s1);
    vector <string> s2 = {"Tycoon Emmanuel", "08098764247"};
    People.addSomeone(s2);
    vector <string> s3 = {"Jaize Informative", "08084837923"};
    People.addSomeone(s3);
    vector <string> s4 = {"Tueday Deji", "07036833446"};
    People.addSomeone(s4);

    cout << People;

    return 0;
}