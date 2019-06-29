def quickSort(array):
    # Write your code here.
	if len(array) <= 1:
		return array
	pivot = array[0]
	left = [i for i in array[1:] if i < pivot]
	right = [j for j in array[1:] if j >= pivot]
	return quickSort(left) + [pivot] + quickSort(right)
