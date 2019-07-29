def searchForRange(array, target):
    # Write your code here.
	rangeIndex = [-1,-1]
	alteredBinarySearch(array, 0, len(array) - 1, rangeIndex, target, True)
	alteredBinarySearch(array, 0, len(array) - 1, rangeIndex, target, False)
	return rangeIndex


def alteredBinarySearch(arr, left, right, rangeIndex, target, goLeft):
	if left > right:
		return
	mid= (left + right) // 2
	if arr[mid] < target:
		alteredBinarySearch(arr, mid + 1, right, rangeIndex, target, goLeft)
	elif arr[mid] > target:
		alteredBinarySearch(arr, left, mid - 1, rangeIndex, target, goLeft)
	else:
		if goLeft:
			if mid == 0 or arr[mid - 1] != target:
				rangeIndex[0] = mid
			else:
				alteredBinarySearch(arr, left, mid - 1, rangeIndex, target, goLeft)
		else:
			if mid == len(arr) - 1 or arr[mid + 1] != target:
				rangeIndex[1] = mid
			else:
				alteredBinarySearch(arr, mid + 1, right, rangeIndex, target, goLeft)
