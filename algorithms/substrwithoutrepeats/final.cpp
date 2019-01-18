#include <iostream>
#include <vector>
#include<map>

using namespace std;

// thi takes linear time 
int lengthOfLongestSubstring(string s) {
        // can be understood as an array of 256 numbers init to -1 
        // k, v
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            // this is the invariant 
            // comparing the value of the char at i to start -1 

            // -1 greater than start -> no 
            if (dict[s[i]] > start)
                // set start to ascii number 
                start = dict[s[i]];
                // start = 2
                // start = 6
                // when start changes so does the max 
                // start gets set to -1 if encountered again 
                cout << "start" <<  start << endl;
            // p 0 -1 -1      start: 0 , 1, 2, 5
            // w 1 0 0
            // w 2 1 1
            // k 3 1 3
            // e 4 1 3
            // w 5 2 3
            // w 6 5 1
            // here we reset
            dict[s[i]] = i;
            // as long as no letter is repeated i increases 
            // when a letter is repeated i decreases 
            cout << (i - start) << endl;
            maxLen = max(maxLen, i - start);
            /*
            some explanation found on leetcode 
            when a letter is repeated then the value of start is first changed to the value at its index in the vector .causing the factor (i-start) to decrease now. 
            due to the reason that value of "i" is still high but start is now also high (in fact one number less than i) so now the value of "i-start" is 1. 
            but this will not cause maxlength to take the 1 ofcourse
            */
        }
        return maxLen;
}


int main() {
    int maxLen = lengthOfLongestSubstring("bbbbb"); 
    cout << maxLen << endl;

    return 0; 
}



