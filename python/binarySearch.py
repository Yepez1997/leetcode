def binarySearch(array, target):
	left = 0
	right = len(array)-1
	while left < right:
		middle = int(left + right / 2)
		if array[middle] == target:
			return middle
		elif array[middle] < target:
			left += 1
		else:
			right -= 1
	return -1

