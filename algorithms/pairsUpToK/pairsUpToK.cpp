#include <iostream>
#include <utility>
#include <vector>

// simple bruteforce approach to pairs that add up to k 
using namespace std; 

typedef pair<int,int> pairs;

// simple brute force approach to unique pairs up to k 
vector<pairs> sumK(vector<int> arr, int k) {
    vector<pairs> results; 
    for (int i = 0; i < ((int)(arr.size())); i++) {
        for (int j = i + 1; j < ((int)arr.size()); j++) {
            if (arr[i] + arr[j] == k) {
                results.push_back(make_pair(i,j));
            }
        }
    }
    return results;
}


int main() {
    vector<int> res; 
    res.push_back(1);
    res.push_back(2);
    res.push_back(5);
    res.push_back(1);
    res.push_back(8);
    res.push_back(4);
    res.push_back(3);
    vector<pairs> sumPairs =  sumK(res, 7);
    for (auto p : sumPairs) {
        cout << "(" << p.first << "," << p.second << ")" << endl; 
    }

    return 0;
}





