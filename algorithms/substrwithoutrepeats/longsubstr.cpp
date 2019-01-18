#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
#include <set>


using namespace std; 

int longestsubstr(map<char,int> hash, string s) {
    vector<int> results;
    map<char,int> copy = hash;
    string holder = "";

    // missing e ? 
    for (int i = 0; i < (int)s.size(); ++i) {
        if (((copy.count(s.at(i))) == 1)) {
            holder += s.at(i);
            copy[s.at(i)] = 0;
            //copy.erase(s.at(i));
        }
        else {
            results.push_back(holder.size());
            holder = "";
             // reset THIS IS THE PART NEEDS FIX x
            // mark current 
            holder += s.at(i);
            cout << holder << endl;
            //copy[s.at(i)] = 0;
            copy = hash;
            copy[s.at(i)] = 0;
        }
    }
    auto max = *max_element(begin(results), end(results)); 
    cout << max << endl; 
    return max; 
}

int main(){
    //string s = "pwwkew";
    string s = "abcabcbb";
    set<char> unique;
    map<char,int> hash;
    for (int i = 0; i < (int)s.size(); ++i) {
        unique.insert(s.at(i));
    }
    
    int set_count = unique.size();
    int count = 1;
    for (int i = 0; i < set_count; ++i){
        hash[s.at(i)] = count;
        count++;
    }
    int maxLen = longestsubstr(hash,s);
    cout <<  maxLen << endl;

    return 0;
}