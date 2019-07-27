def validateBst(tree):
    # Write your code here.
	return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
	# have reached the bottom -> can return true
	if tree is None:
		return True
	# invalid bst property
	if tree.value < minValue or tree.value >= maxValue:
		return False
	return validateBSTHelper(tree.left, minValue, tree.value) and validateBSTHelper(tree.right, tree.value, maxValue)



