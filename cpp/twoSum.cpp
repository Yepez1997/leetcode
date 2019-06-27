using namespace std; 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> indexMaps; 
        vector<int> twoSumPair;
        for (int i = 0; i < nums.size(); i++) {
            indexMaps[nums[i]] = i;
        }
        int complement;
        for (int j = 0; j < nums.size(); j++) {
            complement = target - nums[j];
            if (indexMaps.count(complement) && j != indexMaps[complement]) {
                twoSumPair.push_back(j);
                twoSumPair.push_back(indexMaps[complement]);
                return twoSumPair;
            }
        }
      return twoSumPair;
    }
};
