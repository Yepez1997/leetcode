class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
      counter = collections.Counter(A)
      for k, v in counter.items():
        if v > 1:
          return k
      return -1
