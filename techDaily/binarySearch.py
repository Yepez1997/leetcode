''' Simple implemtation of Binary Search ''' 


# Time Complexiy O(Log n)
class Solution: 
    
    ''' binary search iterative solution '''
    def binarySearchIterative(self, arr, target):
        left = 0
        right = len(arr)-1
        while left < right:
            middle = (left + right) // 2
            if arr[middle] == target:
                return middle
            elif arr[middle] < target:
                left += 1 
            else:
                right -= 1

        return -1 

    ''' binary search recursive solution ''' 
    def binarySearchRecursive(self, arr, left, right, target):
        if left > right:
            return -1
        middle = left + right // 2 
        if arr[middle] < target:
            return self.binarySearchRecursive(arr, left+1, middle, target)
        elif arr[middle] > target:
            return self.binarySearchRecursive(arr, middle, right-1, target)
        else:
            return middle 
        
    
