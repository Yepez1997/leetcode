package program

// O(nm*min(n, m)) time | O(nm*min(n, m)) space
func LongestCommonSubsequence(s1 string, s2 string) string {
	// Write your code here.
	dp := make([][]string, len(s2) + 1)
	for i := range dp {
		dp[i] = make([]string, len(s1) + 1)
	}
	
	for i := 1; i < len(dp); i++ {
		for j := 1; j < len(dp[i]); j++ {
			if (s2[i-1] == s1[j-1]) {
				dp[i][j] = dp[i-1][j-1] + string(s2[i-1])
			} else {
				if (len(dp[i-1][j]) < len(dp[i][j-1])) {
					dp[i][j] = dp[i][j-1]
				} else {
					dp[i][j] = dp[i-1][j]
				}
			}
		}
	}
	return dp[len(s2)][len(s1)]
}
