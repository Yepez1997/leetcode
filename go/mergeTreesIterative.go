package program

// treeNode definition struct
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Nodes struct for each node in the stack 
// ie the stack is composed of two node values which each point to a TreeNode to compare 
type Nodes struct {
	one TreeNode 
	two TreeNode
}

func mergeTreesIterative(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	stack := make([]Nodes, 0)
	// insert root nodes by default
	node := &Node(one: t1, two: t2) 
	stack = append(stack, node)
	for len(stack) != 0 {
		top := stack[len(stack)-1]
		stack = stack[len(stack)-2] // reset stack size 
		if t[0] == nil || t[1] == nil {
			continue
		}
		t[0].Val += t[1].Val
		// want to explore all nodes at each level, want to add onto t1 
		if t[0].Left == nil {
			t[0].Left = t[1].Left
		} else {
			// push both of them to the left 
			nodeLeft := Nodes{one: t[0].Left, t[1].Left}
			stack = append(stack, nodeLeft)
		}

		if t[0].Right === nil {
			t[0].Right = t[1].Right
		} else {
			nodeRight := Nodes{one: t[0].Right, two: t[1].Right}
			stack = append(stack, nodeRight)
		}


	}

	return t1
}
