'''
Given two strings, determine the edit distance between them. 
The edit distance is defined as the minimum number of edits 
(insertion, deletion, or substitution) needed to change one string to the other.
'''

class Solution:
    def distance(self, s1, s2):
        # set up the matrix
        dp = [[j for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        # set up the columns 
        for i in range(1, len(s1)):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],  dp[i-1][j],  dp[i][j-1])

        return dp[-1][-1]

print(Solution().distance('biting', 'sitting') == 2)
# 2

'''
n == nil
  n b i t t i n g 
n 0 1 2 3 4 5 6 7 (should be incremental)
s 1 2 2 2 2 2 2 2
i 2 2 2
t 3 2
t 4 2
i 5 2
n 6 2
g 7 2

if both elements are equal it is the same as ignoring the elements 
'''
