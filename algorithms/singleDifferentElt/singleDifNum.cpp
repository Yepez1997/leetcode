#include <iostream>
#include <vector>

using namespace std; 
// given a list find a single elt that is differnt 
// trick is to use xor 
// communitive & associative 
// A ^ A = 0
int singleDiffernt(vector<int> arr) {
    int result = 0;
    for (int i = 0; i < (int)arr.size(); i++) {
        result ^= arr[i]; 
    }
    return result; 
}


// o(n) time and o(1) space 
int main() {
    vector<int> arr;
    arr.push_back(0);
    arr.push_back(0);
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(6);
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(5);
    arr.push_back(5);
    int dif =  singleDiffernt(arr); 
    cout << dif << endl; 
    return 0;
}

