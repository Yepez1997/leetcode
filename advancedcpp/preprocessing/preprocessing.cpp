#include <iostream>
#include <assert.h>
#include <stdio.h>

// stuff -> minimized globals vars and pass by reference 
// preprocessrors are stuff read before the program 
// is compiled 
// #define macro-name replacement-text 

// #x -> replacement token 
// ## -> concat values 
// predefined macros __Line__ 
#define watch(x) cout << (#x) << " is: " << (x) << '\n'
// functional macros 
#define MAX(x, y) ((x > y) ? x : y)
#define MIN(x, y) (!(x > y) ? x : y)
#define CONCAT(x, y)  x ## y

using namespace std; 

int main() {
    const int x = 20;
    const int y = 25; 
    assert(MAX(x,y) == 25);
    printf("%d\n",MAX(x,y));
    assert(MIN(x,y) == 20);
    printf("%d\n",MIN(x,y));

    string str_one = "ab"; 
    string str_two = "cd"; 

    cout << "Value of __LINE__ : " << __LINE__ << endl;
    cout << "Value of __FILE__ : " << __FILE__ << endl;
    cout << "Value of __DATE__ : " << __DATE__ << endl;
    cout << "Value of __TIME__ : " << __TIME__ << endl;


    
    return 0; 
}