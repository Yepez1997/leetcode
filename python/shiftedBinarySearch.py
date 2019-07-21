def shiftedBinarySearch(array, target):
    # Write your code here.
	return shiftedBinarySearchHelper(array, target, 0, len(array)-1)


def shiftedBinarySearchHelper(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	leftNum = array[left]
	rightNum =  array[right]
	potentialMatch = array[middle]
	if potentialMatch == target:
		return middle
	elif leftNum <= potentialMatch:
		if target >= leftNum and target < potentialMatch:
			return shiftedBinarySearchHelper(array, target, left, middle-1)
		else:
			return shiftedBinarySearchHelper(array, target, middle+1, right)
	else:
		if target <= rightNum and target > potentialMatch:
			return shiftedBinarySearchHelper(array, target, middle+1, right)
		else:
			return shiftedBinarySearchHelper(array, target, left, middle-1)
