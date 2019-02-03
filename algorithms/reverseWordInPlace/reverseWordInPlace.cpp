#include <iostream>
#include <algorithm>

using namespace std;

string reverseWord(string &s) {


    for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
        swap(s[i],s[j]);
    }

    cout << s << endl; 

    return s; 
}




int main() {
    string input = "abcdefg"; // should print gfedcba
    string s = reverseWord(input);
    return 0; 
}