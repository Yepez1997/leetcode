def invertBinaryTree(tree):
	if tree:
		tree.left, tree.right = tree.right, tree.left
		invertBinaryTree(tree.left)
		invertBinaryTree(tree.right)
	return

