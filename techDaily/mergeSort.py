''' Implementaion of Merge Sort in Python '''

# Time Complexity - O(N * LOG N )
class Solution:

    ''' mergeSort - sort an unsorted array using merge sort alg'''
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        middle = (len(arr) // 2)
        left = self.mergeSort(arr[:middle])
        right = self.mergeSort(arr[middle:])
        return self.merge(left, right)

    ''' merge - merge the left and right array '''
    def merge(self, left, right):
        sortedArr = []
        while left and right:
            compare = self.compareVal(left[0], right[0])
            if compare == -1:
                sortedArr.append(left.pop(0))
            else:
                sortedArr.append(right.pop(0))
        for num in left:
            sortedArr.append(num)
        for num in right:
            sortedArr.append(num)
        return sortedArr
    
    ''' compareVal - comparitor helper function ''' 
    def compareVal(self, a, b):
        if a < b:
            return -1
        else:
            return 1 



