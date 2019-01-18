#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>


using namespace std;

typedef map<char,int> hashmap;

// basically keep a count while not in hashmap increase count, if in hashmap
// then we want to reset the count 
int longeststr(string s) {
    hashmap hp; 
    vector<int> result;  
    int longest = 0;
    int count = 0;
    string holder = "";
    for (int i = 0; i < (int)s.size(); ++i) {
        // checks if key is present 
        if ((hp.count(s.at(i)) == 0)) {
            holder += s.at(i);
            hp[s.at(i)] = count;
            ++longest; 
            ++count;
            result.push_back(longest);

        }
        else {
            longest = 0;
            holder = "";

        }

    }
    auto max = *max_element(begin(result), end(result));  
    return max;
}

// ex -> "abcabcbb" -> 3
// ex -> bbbbb" -> 1

int main() {
    string one = "bbbb";
    int one_res = longeststr(one); 
    if (one_res == 1) {
        cout << "Passed 1" << endl;
    }
    string two = "pwwkew";
    int two_res = longeststr(two); 
    cout << two_res << endl;
    if (two_res == 4) {
        cout << "Passed 2" << endl;
    }
    string three= "abcabcbb";
    int three_res = longeststr(three); 
    if (three_res == 3) {
        cout << "Passed 3" << endl;
    }
    return 0;
}