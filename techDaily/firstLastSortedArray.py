class Solution:
    arrRange = [-1, -1]

    def getRange(self, arr, target):    
        # run two binary seach algorithms -> one that forces a left and one that forces a right 
        self.modifiedBinarySearch(arr, 0, len(arr), target, True)
        self.modifiedBinarySearch(arr, 0, len(arr), target, False)
        return self.arrRange

    def modifiedBinarySearch(self, array, left, right, target, goLeft=False):
        # if left > right:
        #     return

        while left <= right:
            middle = (left + right) // 2
            if array[middle] < target:
                left += 1
            elif array[middle] > target:
                right -= 1
            else:
                # middle index is equal now want to check if more values exists for left half
                if goLeft:
                    if middle == 0 or array[middle-1] != target:
                        self.arrRange[0] = middle 
                        return 
                    else:
                        right -= 1
                else:
                    if middle == len(array)-1 or array[middle+1] != target:
                        self.arrRange[1] = middle 
                        return 
                    else:
                        left += 1      



# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
solution = Solution().getRange(arr, x)
print(solution == [1,4])
print(Solution().getRange([100,150,150,153], 150) == [1,2])

# [1, 4]
