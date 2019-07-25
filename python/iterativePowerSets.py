def powerset(array):
    # Write your code here.

	subsets = [[]]
	for ele in array:
		for i in range(len(subsets)):
			currentSubSet = subsets[i]
			subsets.append(currentSubSet + [ele])
	return subsets

