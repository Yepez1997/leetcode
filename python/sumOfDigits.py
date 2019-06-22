class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        minEle = str(min(A))
        sumDigits = sum([int(i) for i in minEle])
        return 1 if sumDigits % 2 == 0 else 0
