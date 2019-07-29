def numberOfBinaryTreeTopologies(n):
    # Write your code here.
	if n == 0:
		return 1
	numberTreeTopologies = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - 1 - leftTreeSize
		leftTopologies = numberOfBinaryTreeTopologies(leftTreeSize)
		rightTopologies = numberOfBinaryTreeTopologies(rightTreeSize)
		numberTreeTopologies += leftTopologies * rightTopologies
	return numberTreeTopologies

