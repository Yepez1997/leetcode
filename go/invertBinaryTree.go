package program


type BinaryTree struct {
	value int

	left  *BinaryTree
	right *BinaryTree
}


func (tree *BinaryTree) InvertBinaryTree() {
	tree.left, tree.right = tree.right, tree.left 
	if (tree.left != nil) {
		tree.left.InvertBinaryTree()
	}
	if (tree.right != nil) {
		tree.right.InvertBinaryTree()
	}
}
