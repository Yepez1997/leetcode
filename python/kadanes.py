def kadanesAlgorithm(array):
    # Write your code here.
	currentMaxSum = array[0]
	maxSum = array[0]
	for i in range(1, len(array)):
		currentMaxSum = max(array[i], array[i] + currentMaxSum)
		maxSum = max(currentMaxSum, maxSum)
	return maxSum

