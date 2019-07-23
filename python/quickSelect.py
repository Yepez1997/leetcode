def quickSort(array, k):
	if len(array) <= 1:
		return array
	if k >= 0:
		pivot = array[0]
		left = [i for i in array[1:] if i < pivot]
		right = [j for j in array[1:] if j >= pivot]
		return quickSort(left, k-1) + [pivot] + quickSort(right,k)
	return

def quickselect(array, k):
	arr = quickSort(array,k+1)
	return arr[k-1]

