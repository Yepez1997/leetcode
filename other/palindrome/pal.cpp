#include <stdio.h>
#include <iostream>
#include <string>

using namespace std; 


bool pal(string s) {
    for (int i = 0, j = s.size() - 1; i < s.length() && j > 0; i++, j--) { 
        if (s[i] != s[j]) {
            return false;
        }
    }
    return true;
}

int main() {
    bool one = pal("abaaba");
    if (one == true) {
        cout << "succes" << endl;
    }
}



