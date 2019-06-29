def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
	stack = []
	while stack or tree:
		if tree:
			stack.append(tree)
			tree = tree.left
		else:
			node = stack.pop()
			callback(node)
			tree = node.right
