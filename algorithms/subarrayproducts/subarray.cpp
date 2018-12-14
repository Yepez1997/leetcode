/* Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays
where the product of all the elements in the subarray 
is less than k.*/

class SubArrayP {
public:
    int numSubarrayProductLessThanK(vector<int> const &nums, int k) {
        if (k <= 1) return 0;
        int prod = 1, ans = 0, left = 0;
        for (int right = 0; right < nums.size(); right++) {
            prod *= nums[right];
            cout << "prod:" << prod << endl;
            while (prod >= k) {
                cout << "enter > k" << endl; 
                prod /= nums[left++];
                cout << "prod < k:" << prod << endl;
            }
            cout << "right: " << right << " left: " << left << endl; 
            ans += right - left + 1;
            cout << "ans: " << ans << endl; 
        }
        return ans;
    }
};
        
