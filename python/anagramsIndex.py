class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        anagramIndex = []
        bIndexMap = {}
        for i in range(len(B)):
          bIndexMap[B[i]] = i
        for i in A:
          anagramIndex.append(bIndexMap[i])
        return anagramIndex
