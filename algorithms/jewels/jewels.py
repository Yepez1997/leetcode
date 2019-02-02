class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jset = set(J)
        # for s in S if s in jset
        return sum(s in jset for s in S)
