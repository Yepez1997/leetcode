def subarraySort(array):
    # Write your code here.
	minElement = float('inf')
	maxElement = float('-inf')
	for i in range(len(array)):
		num = array[i]
		if outOfBounds(array, num, i):
			minElement = min(minElement, num)
			maxElement = max(maxElement, num)
	if minElement == float('inf'):
		return [-1,-1]
	leftIdx = 0
	while minElement >= array[leftIdx]:
		leftIdx += 1
	rightIdx = len(array)-1
	while maxElement <= array[rightIdx]:
		rightIdx -= 1
	return [leftIdx, rightIdx]

# check if an element i is out of bounds
def outOfBounds(arr, num, i):
	if i == 0:
		return num > arr[i+1]
	if i == len(arr)-1:
		return num < arr[i-1]
	return num < arr[i-1] or num > arr[i+1]
