class SingleNumber {
public:
    // testing [1,2]
    int singleNumber(vector<int>& nums) {
     // xor all numbers since x^x = 0 and for all nums 
     // the propery is communitive
     int num = 0;
     for (int i = 0; i < nums.size(); ++i) {
         num ^= nums[i];
     }
     return num;
    }
};

// xor all elts since xor 




