/* Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays
where the product of all the elements in the subarray 
is less than k.*/


/* ALG: First thing is first, set up a right, left, ans variable
 * the right variable is used to iterate through the entire nums vector 
 * every time, we move to the right and the product of the ints is < k (limit value)
 * , the number of indicies that satisfy k is equal to ans += right - left +  1
 * if we are over k, instead of multiplying we start dividing by the left index and incriment
 *  after the value is less than k we proceed to cal ans +=  right - left + 1 again 
 *  repeat all til we are done with the right iteration 
 * */

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
        
