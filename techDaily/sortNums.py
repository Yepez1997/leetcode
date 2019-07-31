"""
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
"""
from collections import Counter

# Time Complexity - O(N) space 
# Space Complexity - O(N) space
def sortNums(nums):
	counter = Counter(nums)
	numOnes = 0
	numTwos = 0
	numThrees = 0
	for k, v in counter.items():    	
		if k == 1:
			numOnes += v
		if k == 2:
			numTwos += v
		if k == 3:
			numThrees += v
	return [1] * numOnes + [2] * numTwos + [3] * numThrees

print(sortNums([3, 3, 2, 1, 3, 2, 1]) == [1, 1, 2, 2, 3, 3, 3])

