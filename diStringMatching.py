class Solution:
    def diStringMatch(self, S: str) -> List[int]:
      # if increase find the smallest avaialable value
      # if decrease find the biggest available value
      n = len(S)
      permutation = list(range(0,n+1))
      result = []
      for instruction in S:
        if instruction == "I":
          result.append(permutation.pop(0))
        else:
          result.append(permutation.pop())

      result += permutation
      return result

