class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      # use a heap to get the top biggest element s ?
      if len(stones) == 1:
        return stones[0]
      stoneHeap = []
      last = 0
      for num in stones:
        heapq.heappush(stoneHeap, -num)
      while stoneHeap:
        if len(stoneHeap) == 1:
            last = -(heapq.heappop(stoneHeap))
        else:
          rockOne = -(heapq.heappop(stoneHeap))
          rockTwo = -(heapq.heappop(stoneHeap))
          print(rockOne, rockTwo)
          if rockOne == rockTwo:
            continue
          else:
            newRock = -rockOne - -rockTwo
            heapq.heappush(stoneHeap, newRock)
      return last

