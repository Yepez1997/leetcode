#include <iostream>
#include <map>
#include <assert.h>
#include <stdio.h>

using namespace std; 

template <typename T>
inline T adder(T x, T y) {
    auto sum = x + y;
    return sum;
}

int main() {
    int x = 9;
    int y = 10;
    auto addTemplate =  adder(x,y);
    assert(addTemplate == 19);
    printf("%s\n", "Passed Case 1");
    return 0; 

}