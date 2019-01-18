#include <iostream>
#include <vector>
#include<map>

using namespace std;

int lengthOfLongestSubstring(string s) {
        // can be understood as an array of 256 numbers init to -1 
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            // this is the invariant 
            // comparing the value of the char at i to start -1 

            // -1 greater than start -> no 
            if (dict[s[i]] > start)
                cout << "s[i]: " << s[i] << endl;
                cout << "dict val: " << dict[s[i]] << endl;
                // set start to ascii number 
                start = dict[s[i]];
                // start = 2
                // start = 6
                // 
                // start gets set to -1 if encountered again 
                cout << "start" <<  start << endl;
            // p - > 1
            // w -> 6
            // k -> 4
            // e -> 5 
            // 
            // here we reset
            dict[s[i]] = i;
            // as long as no letter is repeated i increases 
            // when a letter is repeated i decreases 
            cout << (i - start) << endl;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
}


int main() {
    int maxLen = lengthOfLongestSubstring("pwwkew"); 
    cout << maxLen << endl;

    return 0; 
}



