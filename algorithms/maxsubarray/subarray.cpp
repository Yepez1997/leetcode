// Kadanes Algorithm global and curent sum
class MaxSub {
public:
int maxSubArray(vector<int>& nums) {

        int currentSum = 0, totalSum = INT_MIN;

        for(int i=0; i<nums.size(); i++) {

            //Sum till this point Current Sum till this point + this element
            currentSum = currentSum + nums[i];
            // cs 1
            // cs -1
            // cs 3
            // cs  7
            //If the current maximum array sum is greater than the global total. Update it
            totalSum = max(totalSum, currentSum);
            // ts 1
            // ts 1
            // ts 3
            // ts 7
            //If you get current as less thn 0 then its no point in carrying forward. Make it 0
            currentSum = max(0,currentSum);
            //cs 1
            //cs 0
            //cs 3
            //cs 7

    }
        // 7
        return totalSum;
    }
};
