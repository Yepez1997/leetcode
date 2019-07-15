class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      if nums == None:
        return 0
      j = 0
      while j < len(nums):
        if nums[j] == val:
          del nums[j]
        else:
          j += 1
      return len(nums)
