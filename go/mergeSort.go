package program

func MergeSort(array []int) []int {
	// Write your code here.
	if len(array) <= 1 {
		return array 
	}
	middle := len(array)/2
	
	left := MergeSort(array[:middle])
	right := MergeSort(array[middle:])
	return Merge(left, right)
}

func Merge(left []int, right []int) []int {
	merged := make([]int,0)
	for len(left) != 0 && len(right) != 0 {
		firstLeft := left[0]
		firstRight := right[0]
		switch compare(firstLeft, firstRight) {
			case -1:
			merged = append(merged, firstLeft)
			left = left[1:]
			default:
			merged = append(merged, firstRight)
			right = right[1:]
		}
	}
	for _, val := range left {
		merged = append(merged, val)
	}
	for _, val := range right {
		merged = append(merged, val)
	}
	return merged 
}

func compare(a, b int) int {
	if a < b {
		return -1
	} else {
		return 1 
	}
}

