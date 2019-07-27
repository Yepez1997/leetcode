def maxSumIncreasingSubsequence(array):
    # Write your code here.
	sequence = [None for _ in array]
	sums = [num for num in array]
	maxIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(0,i):
			otherNum = array[j]
			# recall that the j is the element with the less value
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum
				sequence[i] = j
		if sums[i] >= sums[maxIdx]:
			maxIdx = i
	return [sums[maxIdx], getIncreasingSequence(array, sequence, maxIdx)]


def getIncreasingSequence(arr, sequence, currentIdx):
	sequences = []
	while currentIdx is not None:
		sequences.append(arr[currentIdx])
		currentIdx = sequence[currentIdx]
	return list(reversed(sequences))
