// climbing stairs dp problem 

#include <iostream>


using namespace std; 

class Solution {
public:
    
    int climbStairs(int n) {
        if (n == 1) {
            return 1; 
        }   
        int *dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
};


// how many distinct ways can you reach the top 
// can only go up one step
// or can go up two steps 
// what are the possible choices ?
    // if at the ith step 
        // could have came from the last step or the last two steps 
    // either you can take one step 
    // or take two steps 


// Let i be one step, and let j be two step, and let n be the step we want to reach 
// base case: we are at ith step -> 0 
// recursive case: if at the i + 1 th step -> T[n-1]
//                 if  at the i + 2 th step -> T[N-2] + T[N-1]
// First try all of 1's to n 
// Then try yo fit 2's to n by subtracting 1 
// Ie how many twos can we fit if we subtract 1 from n 
// want to keep track of the number of ways we can make a particular value from a set of [T-(n-1)] ets 
// 0 up to the nth position 