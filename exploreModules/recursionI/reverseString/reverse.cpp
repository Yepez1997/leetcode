#include <iostream>
#include <algorithm>

using namespace std; 

// reverses a string 
string reverseString(string& s) {
    for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
        swap(s[i], s[j]);
    }
    return s;
}

int main() {
    string input =  "abbac";
    string output = "cabba";
    
    string reversed = reverseString(input);
    if(reversed == output) {
        cout << "Test Passed" << endl; 

    }
