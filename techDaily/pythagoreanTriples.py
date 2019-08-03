'''

Given a list of numbers, find if there exists a 
pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2
'''

class Solution:
    ''' O(n^2) appraoch ''' 
    def findPythagoreanTriplets(self, nums):
        squared = set([ num ** 2 for num in nums])
        for a in nums:
            for b in nums:
                currentSum = a ** 2 + b ** 2
                if (currentSum in squared):
                    return True 
        return False
        

print(Solution().findPythagoreanTriplets([3, 12, 5, 13]) == True)


# True
