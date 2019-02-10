/*Remove duplicates in vector/array and return the size*/
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>

// could easily convert to a hash set in java 
using namespace std;

// removeDuplicates without set
int removeDuplicates(vector<int>& arr){
    // check for ways to resize an array 
    arr.resize(unique(arr.begin(), arr.end()) - arr.begin());
    return arr.size();  
}

// removeDuplicatesII with a set
int removeDuplicatesII(vector<int>& arr) {
    set<int> s(arr.begin(), arr.end());
    // check over assign significance 
    // http://www.cplusplus.com/reference/vector/vector/assign/
    arr.assign(s.begin(), s.end());
}

// overall O(n) complexity 
int main() {
    return 0;
}



