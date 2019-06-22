import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        kthLargest = None
        for i in range(len(nums)+1-k):
          kthLargest = heapq.heappop(nums)
        return kthLargest


