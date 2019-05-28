package program

import "math"

type BST struct {
	value int

	left  *BST
	right *BST
}

func (tree *BST) Validate() bool {
	return tree.validate(math.MinInt32, math.MaxInt32)
}	

func (tree *BST) validate(min int, max int) bool {
	if tree.value < min || tree.value >= max {
		return false 	
	}
	if tree.left != nil && !tree.left.validate(min, tree.value) {
		return false 	
	}
	if (tree.right != nil && !tree.right.validate(tree.value, max)) {
		return false 	
	}
	return true 
}
