class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
          return 0
        if N == 1:
          return 1
        table = [0 for i in range(N+1)]
        table[1] = 1
        for i in range(2, N+1):
          table[i] = table[i-1] + table[i-2]
        return table[N]
