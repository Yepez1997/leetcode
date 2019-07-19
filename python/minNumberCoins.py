def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	dp = [float('inf') for _ in range(n + 1)]
	dp[0] = 0
	for i in range(1,n+1):
		for j in range(len(denoms)):
			if denoms[j] <= i:
				dp[i] = min(dp[i], dp[i - denoms[j]] + 1)
	return dp[n] if dp[n] != float('inf') else -1

