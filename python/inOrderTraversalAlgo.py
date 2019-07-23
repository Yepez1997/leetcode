# dephtFirstSearch with stack
def iterativeInOrderTraversal(tree, callback):
	stack = []
	while stack or tree:
		if tree:
			stack.append(tree)
			tree = tree.left
		else:
			node = stack.pop()
			callback(node)
			tree = node.right
