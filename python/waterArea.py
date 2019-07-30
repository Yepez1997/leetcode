def waterArea(heights):
	maxes = [0 for _ in heights]
	leftMax = 0
	for i in range(len(heights)):
		height = heights[i]
		maxes[i] = leftMax
		leftMax = max(height, leftMax)
	rightMax = 0
	for j in reversed(range(len(heights))):
		height = heights[j]
		minHeight = min(maxes[j], rightMax)
		if  height < minHeight:
			maxes[j] = minHeight - height
		else:
			maxes[j] = 0
		rightMax = max(rightMax, height)
	return sum(maxes)
