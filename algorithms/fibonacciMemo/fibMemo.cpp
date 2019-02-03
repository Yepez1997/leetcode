#include <iostream>
#include <vector>

#define NIL -1
#define N 100

int lookUpTable[N];

using namespace std; 

void initLookUp() {
    for (int i = 0; i <N; i++) {
        lookUpTable[i] = NIL;
    }
}

// gets the nth fibonaci number
int fib(int n){
    if (lookUpTable[n] == NIL) {
        // compute the values 
        if (n <= 1) {
            lookUpTable[n] = n;
        }
        else {
            lookUpTable[n] = fib(n-1) + fib(n-2);
        }
    }
    return lookUpTable[n];
}


int main() {
    int nthFib = 46; 
    initLookUp();
    // get the 8th fib number 
    int fibNum = fib(nthFib);
    cout << fibNum << endl;
    int count = nthFib; 
    for (auto i : lookUpTable) {
        cout << i  << endl;
        if (count == 0) {
            break;
        }
        count--;
    }
    return 0;
}



// problem determaine if n is in the fib sequence 
// get first 100 fibs 
// create a map and add k:v pairs 
// check if n is in  fib 
// 100 first fibs computed in linear time with memoized version 