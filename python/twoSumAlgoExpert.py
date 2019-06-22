def twoNumberSum(array, targetSum):
    # Write your code here.
	mapIndex = {}
	for i in range(len(array)):
		mapIndex[array[i]] = i
	for j in range(len(array)):
		complement = targetSum - array[j]
		if complement in mapIndex and mapIndex[complement] != j:
			return [complement, array[j]] if complement < array[j] else [array[j], complement]
	return []


