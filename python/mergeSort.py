def mergeSort(array):
    # Write your code here.
	if len(array) <= 1:
		return array
	middle = len(array) // 2
	left = mergeSort(array[:middle])
	right = mergeSort(array[middle:])
	return merge(left, right)

def merge(left, right):
	sortedArray = []
	while len(left) > 0 and len(right) > 0:
		# essentially compare values here
		val = compare(left[0], right[0])
		if val == -1:
			sortedArray.append(left.pop(0))
		else:
			sortedArray.append(right.pop(0))

	sortedArray += left
	sortedArray += right
	return sortedArray


def compare(a, b):
	return -1 if a < b else 1


