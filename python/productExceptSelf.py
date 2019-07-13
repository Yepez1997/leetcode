class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      numsLen = len(nums)
      l, r = [0] * numsLen, [0] * numsLen

      # set up left half
      l[0] = 1
      for i in range(1, numsLen):
        l[i] = l[i-1] * nums[i-1]

      # set up right half
      r[numsLen-1] = 1
      for j in reversed(range(numsLen - 1)):
        r[j] = r[j+1] * nums[j+1]

      # combine the products for both the left and right half
      for k in range(numsLen):
        nums[k] = l[k] * r[k]

      return nums
