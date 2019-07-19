func productExceptSelf(nums []int) []int {
	// the premise of the problem is to calculate left and right subarrays
	left := make([]int, len(nums))
	right := make([]int, len(nums))

	// find all the products left of array
	left[0] = 1
	for i := 1; i < len(nums); i++ {
		left[i] = left[i-1] * nums[i-1]
	}

	// find all products right of the array
	right[len(nums)-1] = 1
	for j := len(nums) - 2; j >= 0; j-- {
		right[j] = right[j+1] * nums[j+1]
	}

	result := make([]int, len(nums))
	for i := range result {
		result[i] = left[i] * right[i]
	}

	return result
}
