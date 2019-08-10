''' quickSort - sort a list using quickSort ''' 

class Solution:
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [num for num in arr[1:] if num < pivot]
        right = [num for num in arr[1:] if num >= pivot]
        return self.quickSort(left) + [pivot] + self.quickSort(right)

def main():
    arr = [2,4,6,1,5,3]
    solution = Solution().quickSort(arr)
    print(solution)
    print(solution == [1,2,3,4,5,6])
    return 0



main()



