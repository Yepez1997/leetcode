"""
You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.
"""

def two_sum(arr, k):
    complements = {}
    for num in arr:
        # assuming the numbers are unique 
        complements[num] = arr.index(num)
    for num in arr:
        complement = k - num
        if complement in complements:
            return True 
    return False

print(two_sum([4,7,1,-3,2], 5) == True)
