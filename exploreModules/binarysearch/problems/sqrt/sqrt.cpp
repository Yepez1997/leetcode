#include <iostream>
#include <vector>

using namespace std;

int sqrtBinarySearch(int num) {

    int low = 0;
    int high, mid = num;

    if (num < 2) {
        return num;
    }
    while (low <= high) {
        mid = (low + high) / 2;

        if (num/mid >= mid) {
            low = mid + 1;
        }
        else {
            high = mid;
        }
    }
    return high - 1;
}

// first 
// 8 -> 
// low = 0; high, mid = 8 
// mid =  4 
// num/mid -> 8/4 -> 2 -> 
// high = mid = 4

// second
// 8 ->
// mid = 0 + 4 / 2 = 2
// 8 / 2  = 4 -> 
// 4 > 2
// low = 2 + 1
// low = 3 
// loop still continues since 3 < 4 


int main(){
    return 0;
}