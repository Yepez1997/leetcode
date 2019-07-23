# Longest Common Subsequence 
def lcs(str1, str2):
    dp =  [[0 for j in range(len(str1)+1)] for i in range(len(str2)+1)]
    for r in range(len(str2)+1):
        for c in range(len(str1)+1):
            if r == 0 or c == 0:
                dp[r][c] = 0
            if str1[r-1] == str2[c-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = max(dp[r-1][c-1], dp[r-1][c])
    return dp[len(str1), len(str2)]
