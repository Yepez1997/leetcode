def fourNumberSum(array, targetSum):
    # Write your code here.
	allPairSums = {}
	quadruplets = []


	for i in range(1, len(array)-1):
		for j in range(i+1, len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if difference in allPairSums:
				pairs = allPairSums[difference]
				for pair in pairs:
					quadruplets.append(pair + [array[i]] + [array[j]])
		# still in the i loop
		for k in range(0, i):
			currentSum = array[i] + array[k]
			if currentSum not in allPairSums:
				allPairSums[currentSum] = [[array[k], array[i]]]
			else:
				allPairSums[currentSum].append([array[k], array[i]])
	return quadruplets

