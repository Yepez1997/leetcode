def maxProfitWithKTransactions(prices, k):
    # Write your code here.
	if len(prices) == 0:
		return 0
	dp = [[0 for x in prices] for i in range(k+1)]
	for t in range(1, k+1):
		maxThusFar = float("-inf")
		for p in range(1, len(prices)):
			maxThusFar = max(maxThusFar, dp[t-1][p-1] - prices[p-1])
			dp[t][p] = max(dp[t][p-1], maxThusFar + prices[p])
	return dp[-1][-1]

