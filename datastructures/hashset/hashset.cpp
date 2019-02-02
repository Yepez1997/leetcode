#define MAX_LEN 100000  

 // the amount of buckets
 #include <vector>
 #include <iostream>

 using namespace std; 
 
class MyHashSet {
private:
    vector<int> set[MAX_LEN];   // hash set implemented by array
    
    /** Returns the corresponding bucket index. */
    // hashfunction can vary per application 
    int getIndex(int key) {
        return key % MAX_LEN;
    }
    
    /** Search the key in a specific bucket. Returns -1 if the key does not existed. */
    int getPos(int key, int index) {
        // Each bucket contains a list. Iterate all the elements in the bucket to find the target key.
        // iterate through all the elements in the bucket 
        for (int i = 0; i < set[index].size(); ++i) {
            if (set[index][i] == key) {
                return i;
            }
        }
        return -1;
    }
public:
    /** Initialize your data structure here. */
    MyHashSet() {     
        
    }
    
    /*adds key to bucket */
    void add(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos < 0) {
            // Add new key if key does not exist.
            // push back keys to the list of arrs for the paritucalt index 
            set[index].push_back(key);
        }
    }
    
    /*removes ket from the bucket*/
    void remove(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos >= 0) {
            // Remove the key if key exists.
            set[index].erase(set[index].begin() + pos);
        }
    }
    
    /** Returns true if this set did not already contain the specified element */
    bool contains(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        return pos >= 0;
    }
};

/**
 * MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * bool param_3 = obj.contains(key);
 */

int main() {
    return 0;
}


