package program

import "math"

type BST struct {
	value int

	left  *BST
	right *BST
}

func (tree *BST) FindClosestValue(target int) int {
	queue := []*BST{tree}
	nodeVal := tree.value
	closest := abs(tree.value, target)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if abs(node.value, target) <= closest {
			closest = abs(node.value, target)
			nodeVal = node.value
		}
		if node.left != nil {
			queue = append(queue, node.left)
		}
		
		if node.right != nil {
			queue = append(queue, node.right)
		}
	}
	return nodeVal
}

func abs(a, b int) int {
	out := math.Abs(float64(a) - float64(b))
	return int(out)
}
