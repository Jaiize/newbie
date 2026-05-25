#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

#define DEBUG
#define age = 44
#define think(a, b) ((a > b) ? a : b)
#define MKSTR(name) #name
#define concat(x, y) x ## y

int main(){

    srand(time(0)); // Change random number on each second
    for(int i = 0; i < 5; i++){
        // cout << rand()%6 << endl;
    }

    int a, b;
    a = 10;
    b = 15;
    int xy = 123;
    int get = 234;

#ifdef DEBUG
    cerr << "Trace: Inside the main function" << endl;
#endif

#if 0
    // Code prevented from compiling
    </>
#endif

    cout << "The max. is: " << think(a, b) << endl;
    cout << MKSTR(Joseph Tosin) << endl;
    cout << "Concatenation function: " << concat(x, y) << endl;
    cout << "Concatenation function: " << concat(ge, t) << endl;
    cout << "Concatenation function: " << concat(g, et) << endl;
    cout << "The line is: " << __LINE__ << endl;
    cout << "The file name is: " << __FILE__ << endl;
    cout << "The date is: " << __DATE__ << endl;
    cout << "The time is: " << __TIME__ <<  endl;
    
#ifdef DEBUG
    cerr << "Trace: Coming out of main function" << endl;
#endif

#if 0
    // Modifiers
    unsigned long int m;
    signed long int n;
    unsigned short int o;
    signed short int p;

    unsigned q;
    short r;
    long r;

    unsigned int a;
    signed int b;
    short int c;
    long int d;

    unsigned char e;
    signed char f;

    long double op;
#endif  

    cin.get();
    system("pause");
    return 0;
}
