class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        row = 0
        while row < len(intervals) - 1:
            if intervals[row][1] >= intervals[row+1][0]:
                intervals[row][1] = max(intervals[row+1][1], intervals[row][1])
                del intervals[row+1]
            else:
                row += 1
        return intervals

