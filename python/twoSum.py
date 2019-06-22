class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
          map[nums[i]] = i
        for j in range(len(nums)):
          complement = target - nums[j]
          if complement in map and map[complement] != j:
              return [j, map[complement]]
        return -1
