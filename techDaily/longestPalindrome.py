"""
A palindrome is a sequence of characters that reads the same backwards and forwards.
Given a string, s, find the longest palindromic substring in s.
"""

class Solution:
    """ longestPalidrome - get the longest palindrome in a string """
    def longestPalindrome(self, s):
        longestPalindromeIndex = [0,1]
        for i in range(1, len(s)):
            oddLen = self.expandString(s, i-1, i+1)
            evenLen = self.expandString(s, i-1, i)
            currentLongestPalindromeIndex = max(oddLen, evenLen, key = lambda a: a[1] - a[0])
            longestPalindromeIndex =  max(currentLongestPalindromeIndex, longestPalindromeIndex,  key = lambda a: a[1] - a[0])
        # print(s[longestPalindromeIndex[0]: longestPalindromeIndex[1]])
        return s[longestPalindromeIndex[0]: longestPalindromeIndex[1]]

    """ expandString - expand from the current index"""
    def expandString(self, s, leftIdx,rightIdx):
        # should return coordintates
        while leftIdx >= 0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
            leftIdx -= 1
            rightIdx += 1
        return [leftIdx + 1, rightIdx]


s = "tracecars"
print(str(Solution().longestPalindrome(s)) == "racecar")
t = "million"
print(str(Solution().longestPalindrome(t)) == "illi")
k = "banana"
print(str(Solution().longestPalindrome(k)) == "anana")


