package program



// leftMax: returns the left maxes in the array 
func leftMax(heights []int) []int {
	leftMaxArr := make([]int, 0)
	leftMaxNum := heights[0]
	leftMaxArr = append(leftMaxArr, 0)
	for i := 0; i < len(heights); i++ {
		currentHeight := heights[i] 
		if currentHeight > leftMaxNum {
			leftMaxNum = currentHeight 
			leftMaxArr = append(leftMaxArr, leftMaxNum)
		} else {
			if i != 0 {
				leftMaxArr = append(leftMaxArr, leftMaxArr[i-1])
			}
		}
	}
	return leftMaxArr
}

// rightMax: returns the rigth max in the array 
func rightMax(heights []int) []int {
	rightMaxArr := make([]int, 0)
	rightMaxNum := heights[len(heights)-1]
	rightMaxArr = append([]int{0}, rightMaxArr...)
	for j := len(heights)-1; j > 0; j-- {
		currentHeight := heights[j]
		if (currentHeight > rightMaxNum) {
			rightMaxNum = currentHeight
			rightMaxArr = append([]int{rightMaxNum}, rightMaxArr...)
		} else {
				rightMaxArr = append([]int{rightMaxArr[0]}, rightMaxArr...)
			} 
		}
	return rightMaxArr
}

func WaterArea(heights []int) int {
	if len(heights) == 0 {
		return 0
	}
	leftMaxWater := leftMax(heights)
	rightMaxWater := rightMax(heights)
	
	waterArr := make([]int,0)
	for i := 0; i < len(leftMaxWater); i++ {
		currentHeight := heights[i]
		minHeight := min(leftMaxWater[i], rightMaxWater[i])
		if (currentHeight < minHeight) {
			waterArr = append(waterArr, minHeight - currentHeight)
		} else {
			waterArr = append(waterArr, 0)
		}
	}
	
	return sum(waterArr)
}

// sum: sum elts in an array (helper method)
func sum(a []int) int {
	total := 0
	for _, v := range a {
		total += v
	}
	return total
}

// min: gets the minimum elt (helper method)
func min(a, b int) int {
	if a < b {
		return a 
	} else {
		return b
	}
}

