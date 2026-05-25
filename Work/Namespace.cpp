#include <iostream>

using namespace std;

namespace Jaize{
    void tosin(int x){
        cout << "print out tosin: " << x << endl;
    }
    namespace Jaize2{
        void tosin2(int x){
            cout << "Print out tosin 2: " << x << endl;
        }
    }

}

namespace Josephet{
    void tosin(int x){
        cout << "print out tosin 3: " << x << endl;
    }
    int rat(int x, int y){
        return(x > y ? x : y);
    }
}

//using namespace Jaize; for tosin()
//using namespace Jaize::Jaize2; for tosin2()
//using namespace Josephet; for tosin
int main(){

    Jaize::tosin(14);
    Jaize::Jaize2::tosin2(45);
    Josephet::tosin(18);
    cout << Josephet::rat(78, 20) << endl;
    
    //tosin();
    //tosin2();
    //tosin();


    return 0;
}