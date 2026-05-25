#include <iostream>
#include <map>
#include <vector>
#include <array>


using namespace std;

int main(){
  
   array <int, 6> man = {4, 5, 6, 7, 4, 9};
   int n = man.size();
     
    cout << "Array = [ " ;
   for(int x = 0; x < n; ++x){
    cout << man[x] << " ";
   }
   cout << "]";
   cout << endl;
   
   vector <bool> visited(n + 1);

   cout << "Duplicate Found: ";
   
   for(auto i: man){
     if(visited[i]){
        // rerturn i (if "int")
          cout << i << " " ;
     }
     visited[i] = true;
   }
   cout << endl;
/*
or
array <int, 8> man = {1, 5, 8, 6, 3, 8, 2, 9};
  map <int, int> map;
  for(auto i: man){
    if(map.find(i) != map.end()){
        map[i]++;
    }else{
      map[i] = 1;
    }

  }
  
  cout << "Duplicate Found: ";
  for(auto x: map){
    if(x.second == 2){
        cout << x.first << endl;
    }
  }
  cout << endl;




*/

  // Free container
  cout << '\n';
  initializer_list <int> nums = {8, 5, 6, 2, 1};
  int n = nums.size();

  initializer_list <int> :: iterator itr;
  for(itr = nums.begin(); itr != nums.end(); itr++){
      cout << *itr << " ";
  }

    return 0;
}