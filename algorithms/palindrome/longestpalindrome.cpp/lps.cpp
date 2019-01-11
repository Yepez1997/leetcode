#include <iostream>
#include <vector>
#include <exception>

/*
Longest Palindrome Sequence 
Given a string determaine the longest palindrome -> words that match start to end 

*/

using namespace std; 

string longestPalindrome(string s) {
    string T; 
    for (int i = 0; i < s.size(); i++) {
        T+="#"+s.substr(i,1); 
    }
    T.push_back('#'); 

    vector<int> P(T.size(), 0);
    int center = 0, boundary = 0, maxLen = 0, resCenter = 0;

    for (int i = 1; i < T.length() - 1; i++) {
        int mirror = 2 * center - i; 
        P[i] = (boundary > i) ? min(boundary - i, P[mirror]): 0;
        while (i - 1 - P[i] >= 0 && i + 1 + P[i] <= T.size() - 1 && T[i + 1 + P[i]] == T[i - 1 - P[i]]) {
            P[i]++;
        }
        if (i + P[i] > boundary) {
            center = i; 
            boundary = i + P[i]; 
        }

        if (P[i] > maxLen) {
            maxLen = P[i];
            resCenter = i;
        }
    }

    return s.substr((resCenter - maxLen)/2, maxLen);
}






