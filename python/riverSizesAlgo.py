def riverSizes(matrix):
	riverSizes = []
	seen = [[False for value in row] for row in matrix]
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if seen[row][col]:
				continue
			if not seen[row][col] and matrix[row][col] == 1:
				riverSizes.append(exploreDFS(row, col, matrix, seen))
	return riverSizes


def exploreDFS(row, col, matrix, seen):
	if (col < 0 or row < 0 or row + 1 > len(matrix) or col >= len(matrix[row]) or seen[row][col] or matrix[row][col] != 1):
		return 0
	seen[row][col] = True
	return 1 + exploreDFS(row+1,col, matrix, seen) + exploreDFS(row-1,col, matrix, seen) + exploreDFS(row,col+1, matrix, seen) + exploreDFS(row,col-1, matrix, seen)




