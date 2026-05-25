#include <iostream>

using namespace std;

int main(){

    char x;
    //char lc, uc;

    //LOOP: 
    cout << "Enter a character to check if it's a consonant or vowel letter!" << endl;
    cin >> x;

    //lc = (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u');
    //uc = (x == 'A' || x == 'E' || x == 'I' || x == 'O' || x == 'U');



    // Switch method
    switch(x){
        case 'a':
        cout << x << ": is a vowel letter in lower case!" << endl;
        break;
        case 'e':
        cout << x << ": is a vowel letter in lower case!" << endl;
        break;
        case 'i':
        cout << x << ": is a vowel letter in lower case!" << endl;
        break;
        case 'o':
        cout << x << ": is a vowel letter in lower case!" << endl;
        break;
        case 'u':
        cout << x << ": is a vowel letter in lower case!" << endl;
        break;
        case 'A':
        cout << x << ": is a vowel letter in upper case!" << endl;
        break;
        case 'E':
        cout << x << ": is a vowel letter in upper case!" << endl;
        break;
        case 'I':
        cout << x << ": is a vowel letter in upper case!" << endl;
        break;
        case 'O':
        cout << x << ": is a vowel letter in upper case!" << endl;
        break;
        case 'U':
        cout << x << ": is a vowel letter in upper case!" << endl;
        break;
        case 'b':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'B':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'c':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'C':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'd':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'D':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'f':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'F':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'g':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'G':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'h':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'H':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'j':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'J':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'k':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'K':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'l':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'L':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'm':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'M':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'n':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'N':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'p':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'P':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'q':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'Q':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'r':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'R':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 's':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'S':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 't':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'T':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'v':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'V':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'w':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'W':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'x':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'X':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'y':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'Y':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'z':
        cout << x << ": is a consonant letter" << endl;
        break;
        case 'Z':
        cout << x << ": is a consonant letter" << endl;
        break;
        // Loop purposes
        //case '.':
        //goto FIN;
        //break;

        default:
        cout << x << ": is neither a vowel nor consonant letter" << endl;
        break;

    }

    //goto LOOP;



    //if(x == '0'){
    //    cout << x << ": is not a character!" << endl;
    //}

    // Continuous / Loop method
    /*while(x != '0'){
    
        if(lc){
            cout << x << " is a vowel letter in lower case!" << endl;
            goto LOOP;
        }

        if(uc){
            cout << x << " is a vowel letter in upper case!" << endl;
            goto LOOP;
        }
        
        cout << x;
        if(!(x = lc && uc)){
            cout << " is not a vowel letter!" << endl;
            goto LOOP;
        }

    }*/


    // Regular / Simple method
    /*while(x != '0'){
    
        if(lc){
            cout << x << " is a vowel letter in lower case!" << endl;
            break;
        }

        if(uc){
            cout << x << " is a vowel letter in upper case!" << endl;
            break;
        }
        
        cout << x;
        if(!(x = lc && uc)){
            cout << " is not a vowel letter!" << endl;
            break;
        }

    }*/

   
    //FIN:
    //system("pause");
    return 0;
}