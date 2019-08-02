''' 
    Given an array of integers, return a new array such that each element at index
    i of the new array is the product of all the numbers in the original array 
    except the one at i 
'''


class Solution:
    def productExceptSelf(self, arr):
        n =  len(arr)
        results = [1] * n 
        left  = [1] * n 
        right = [1] * n 

        # get the product of all the left 
        for i in range(1,  n):
            left[i] = left[i-1] * arr[i-1]

        # get the products of all the right 
        for j in reversed(range(n-1)):
            right[j] = right[j+1] * arr[j+1]

        # merge the products 
        for k in range(n):
            results[k] = left[k] * right[k]
        return results 

print(Solution().productExceptSelf([3,2,1]) == [2,3,6])
