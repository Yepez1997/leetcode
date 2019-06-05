package program

type BinaryTree struct {
	value int

	left  *BinaryTree
	right *BinaryTree
}

func (tree *BinaryTree) InvertBinaryTree() {
	queue := []*BinaryTree{tree}
	for len(queue) > 0 {
		elt := queue[0]
		queue = queue[1:]
		if (elt == nil) {
			continue 
		}
		elt.left, elt.right = elt.right, elt.left
		queue = append(queue, elt.left, elt.right)
	}
}

