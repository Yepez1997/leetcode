/* Given an array of positive integers nums.
Count and print the number of (contiguous) 
subarrays where the product of all the elements 
in the subarray is less than k.*/

class SubArrayProductsn {
public:
    int numSubarrayProductLessThanK(vector<int> const &nums, int k) {
        if (k <= 1) return 0;
        int prod = 1, ans = 0, left = 0;
        for (int right = 0; right < nums.size(); right++) {
            prod *= nums[right];
            while (prod >= k) prod /= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    }
};

