''' Simple implemtation of Binary Search ''' 

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

    ''' binary search recursive solution ''' 
    def binarySearchRecursive(self, arr, left, right, target):
        if left > right:
            return -1
        middle = left + right // 2 
        if arr[middle] < target:
            self.binarySearchRecursive(arr, left, middle - 1, target)
        elif arr[middle] > target:
            self.binarySearchRecursive(arr, middle + 1, right, target)
        else:
            return middle 
        
    
