# longestPalindrome in o(n^2) time -> improvement from an o(n^3)
def longestPalindromicSubstring(string):
	currentLongest = [0,1]
	for i in range(1, len(string)):
		odd = getLongestPalindrome(string, i-1, i+1)
		even = getLongestPalindrome(string, i-1,i)
		longest = max(odd, even, key = lambda x : x[1] - x[0])
		currentLongest = max(currentLongest, longest, key = lambda x : x[1] - x[0])
	return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindrome(string, leftindx, rightindx):
	while leftindx >= 0 and rightindx < len(string):
		if string[leftindx] != string[rightindx]:
			break
		leftindx -= 1
		rightindx += 1
	return [leftindx + 1, rightindx]

