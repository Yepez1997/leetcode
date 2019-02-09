/*TwoSum : find two ints in array the add to target */ 

/* Commonly used in interviews */

/* ALG : In essence iterate a map 
 *  for every first value, subtract from target
 *  the result from target - first should be present in the map 
 *  if it is present, we are done hence two sum else ...*/

#include <iostream>
#include <map> 
#include <vector> 
#include <iterator>

using namespace std;
// multimap can have mulitple elts with the same key 
// builds a hash table with linked list 
vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result; //return vector
    multimap<int, int> map; //<value, index>
        
    //insert values & indices into map
    for (unsigned int i = 0; i < nums.size(); ++i){
        map.insert(std::make_pair(nums[i], i));
    }
        
    //iterate through map
    for(auto it = map.begin(); it != map.end(); ++it){
        int findMe = target - it->first;
        auto found = map.find(findMe);
        if(found != map.end() && found != it){
            v = {it->second, found->second};
            std::sort(v.begin(), v.end()); //sort indices into ascending order...
            return result;
        }
    }
        return result;
}


