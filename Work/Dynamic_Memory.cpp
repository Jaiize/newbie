#include <iostream>

using namespace std;

class Jaz{
    public:
    Jaz(){
        cout << "Constructor" << endl;
    }
    ~Jaz(){
        cout << "Destructor" << endl;
    }

};

int main(){
    Jaz* bob = new Jaz[2]; 

    delete [] bob;

    
    double* pvalue = NULL; // double* pvalue = new double;
    pvalue = new double;

    // for checking
    if (!(pvalue = new double)){
        cerr << "Error: out of memory" << endl;
        exit(1);
    }else{
        cout << "Memory allocated successfully!" << endl;
    }

    *pvalue = 25.254;
    cout << "Value is: " << *pvalue << endl;

    delete pvalue;

    
    //char* nvalue = new char[10];
    //delete [] nvalue;
     

    return 0;
}