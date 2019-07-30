""" Find the duplicate number in the array """



""" singleNumber - finds the duplicate number in the array """
def singleNumber(nums):
    result = 0 
    for num in nums:
        result ^= num
    return result
      
""" Use XOR to achieve constant space 
    In Boolean Algebra expression can be communitve and associative 
    a ^ a = 0
    a ^ 0 = a
"""

print(singleNumber([4, 3, 2, 4, 1, 3, 2]) == 1)
print(singleNumber([1, 1, 1, 1, 1, 1, 2]) == 2)
