/*TwoSum : find two ints in array the add to target */ 

/* Commonly used in interviews */

/* ALG : In essence iterate a map 
 *  for every first value, subtract from target
 *  the result from target - first should be present in the map 
 *  if it is present, we are done hence two sum else ...*/

class TwoSum {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> result; //return vector
        std::multimap<int, int> map; //<value, index>
        
        //insert values & indices into map
        for (unsigned int i = 0; i < nums.size(); ++i){
            map.insert(std::make_pair(nums[i], i));
        }
        
        //iterate through map
        for(auto it = map.begin(); it != map.end(); ++it){
            cout << "target: " << target << endl; 
            int findMe = target - it->first;
            cout << "it->first: " << it->first << endl; 
            cout << "find me: " << findMe << endl;
            auto found = map.find(findMe);
            //cout << found << endl; 
            if(found != map.end() && found != it){
                cout << "******" << endl; 
                cout << "found->second: " << found->second << endl; 
                cout << "it->second: " << it->second << endl; 
                v = {it->second, found->second};
                std::sort(v.begin(), v.end()); //sort indices into ascending order...
                return result;
            }
        }
        return result;
    }

}
