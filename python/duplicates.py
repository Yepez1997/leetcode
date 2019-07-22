class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counterObj = collections.Counter(nums)
        duplicates = []
        for k, v in counterObj.items():
          if v == 2:
            duplicates.append(k)
        return sorted(duplicates)
