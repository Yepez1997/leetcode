#include <iostream>
#include <stack>
#include <vector>


using namespace std; 

inline int MAX(int x, int y) {
    return (x > y ? x : y); 
}

// string is from index i ... j 
// recurse left and rigth and find the max 
inline int lcs(vector<string>& str, int i, int j){
    if (i == 0 || j == 0) {
        return 0;
    }
    else if (str[i] == str[j]) { 
        return 1 + lcs(str, i - 1, j - 1); 
    }
    else {
        return MAX(lcs(str, i - 1, j), lcs(str, i , j - 1));
    }
    return 0;
}

int main() {

    // 
    int i = 
    return 0;
}




