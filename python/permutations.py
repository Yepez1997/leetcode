def getPermutations(array):
    # Write your code here.
	permutations = []
	getPermutationsHelper(array, [], permutations)
	return permutations

def getPermutationsHelper(arr, currentPermutation, permutations):
	if not len(arr) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(arr)):
			newArr = arr[:i] + arr[i+1:] # not including i
			newPermutation = currentPermutation + [arr[i]] # including i
			getPermutationsHelper(newArr, newPermutation, permutations)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permuteNums = self.getPermutations(nums,[], permutations)
        return permutations

    def getPermutations(self, arr, permutation, permutations):
      if len(arr) == 0:
        permutations.append(permutation)
      else:
        for i in range(len(arr)):
          newArr = arr[:i] + arr[i+1:] # without i
          newPermutation = permutation + [arr[i]]
          self.getPermutations(newArr, newPermutation, permutations)

