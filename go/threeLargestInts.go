package program
import "math"

func FindThreeLargestNumbers(array []int) []int {
	// Write your code here.
	three := []int{math.MinInt32, math.MinInt32, math.MinInt32}
	for _, v := range array {
		UpdateLargest(v, three)
	}
	return three 
}

func UpdateLargest(num int, largest []int) {
	if num > largest[2] {
		ShiftAndUpdate(num, 2, largest)
	} else if num > largest[1] {
		ShiftAndUpdate(num, 1, largest)
	} else if num > largest[0] {
		ShiftAndUpdate(num, 0, largest)
	}
}

func ShiftAndUpdate(num int, idx int, array []int) {
	for i := 0; i < idx + 1; i++ {
		if idx == i {
			array[i] = num
		} else {
			array[i] = array[i+1]
		}
	}
}
