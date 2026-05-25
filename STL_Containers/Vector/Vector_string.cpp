#include <iostream>
#include <vector>
#include <string>

using namespace std;

        
void solution(vector <vector<string>> students){

        vector <string> P1 = {"Joseph", "-", "Lokoja, Kogi-State", "Nigeria."};
        students.push_back(P1);
        vector <string> P2 = {"Tosin", "-", "Lokoja, Kogi-State", "Nigeria."};
        students.push_back(P2);
        vector <string> P3 = {"Emmanuel", "-", "Lokoja, Kogi-State", "Nigeria."};
        students.push_back(P3);
        for(vector <string> D: students){
                for(int x = 0; x < D.size(); x++){
                        cout << D[x] << " ";
                }
               
                cout << "\n\t\t\t";

        }

}


vector <string> man(){
    return {"Hello, world!", "Joseph Tosin"};
}

int main(){
        
    vector <vector<string>> students;
    cout << "Solution :  ";
    solution(students);

    // vector <string> p = man();
    auto p = man();
    cout << p[0] << endl;


    
    return 0;
}