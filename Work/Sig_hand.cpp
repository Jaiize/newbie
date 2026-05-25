#include <iostream>
#include <csignal>

using namespace std;

// void (*signal (int sig, void (*func) (int))) (int);

void signalHandler(int sig){
    cout << "Interrupt signal: " << sig << " received" << endl;
    exit(sig);
}

int main(){

    int x = 0;    
    signal(SIGINT, signalHandler);
    
    while(++x){
        cout << "Going to sleep..." << endl;
        if(x == 3){
            raise(SIGINT);
        }
        // sleep(1); does not work or recognise
    }

#if 0
    SIGINT 2
    SIGILL 4
    SIGABRT_COMPAT 6
    SIGFPE 8
    SIGSEGV 11
    SIGTERM 15
    SIGBREAK 21
    SIGABRT 22
    SIGHUP // unknown
#endif
    

    // system("pause");
    return 0;
}