#include <iostream>
#include <unordered_map>
#include <map>

using namespace std;

struct CityRecord{


    string name;
    uint64_t population;
    double lat, lon;

    bool operator > (const CityRecord& other) const {
        return(this->population > other.population);
    }
        
};

namespace std{
    
    template<>
    struct hash <CityRecord> {
        size_t operator()(const CityRecord& key) {
        
        return (hash <string>()(key.name));

        }
    };
}

int main(){

    /*vector <CityRecord> box;
    box.emplace_back("Lagos", 500000, 5.3, 4.5);
    box.emplace_back("Abuja", 400000, 5.3, 4.5);
    box.emplace_back("Ibadan", 525000, 5.3, 4.5);
    box.emplace_back("portharcout",300000, 5.3, 4.5);

    for(const auto& fetch: box){
        if(fetch.name == "Abuja"){
            fetch.population;
            break;
        }
    }*/

    //for the weird (hash function) template
    //map <CityRecord, uint32_t> founded;

    map <string, CityRecord> list;

    list["Lagos"] = {"Lagos", 500000, 5.3, 4.5};
    list["Abuja"] = {"Abuja", 400000, 5.3, 4.6};
    list["Ibadan"] = {"Ibadan", 525000, 5.3, 4.2};
    list["porthacourt"] = {"portharcout", 300000, 5.3, 4.7};

    //CityRecord & lData = list["Lagos"];
    //cout << lData.lat;

    //Structure Binding
    for(const auto& [name, city]: list){
        cout << name << "Population - " << city.population << endl;
    }
    cin.get();

    /*for(auto & kv: list){
        const string & name = kv.first;
        CityRecord & city = kv.second;
        cout << kv.first << " ";
        cout << city.population << " ";
        cout << city.lat << " ";
        cout << city.lon << endl;
    }*/
    

      
   
    return 0;
}