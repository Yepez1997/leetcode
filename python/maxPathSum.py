def maxPathSum(tree):
	_, maxPath = findMaxSum(tree)
	return maxPath

def findMaxSum(tree):
	if tree is None:
		return (0,0)
	leftMaxSumAsBranch, leftMaxSum = findMaxSum(tree.left)
	rightMaxSumAsBranch, rightMaxSum = findMaxSum(tree.right)
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
	maxSumAsBranch = max(tree.value, maxChildSumAsBranch + tree.value)
	maxSumAsRoot = max(maxSumAsBranch, leftMaxSumAsBranch + tree.value + rightMaxSumAsBranch)
	maxPathSum = max(leftMaxSum, rightMaxSum, maxSumAsRoot)
	return (maxSumAsBranch, maxPathSum)

