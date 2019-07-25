def searchInSortedMatrix(matrix, target):
    # Write your code here.
	row = 0
	col = len(matrix[0])-1 # last element in the col
	# invariant in bounds
	while col >= 0 and row < len(matrix):
		if matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1
		else:
			return [row, col]
	return [-1,-1]


