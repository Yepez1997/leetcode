package program

type node struct {
	min int 
	max int 
}

type MinMaxStack struct {
	// Write your code here.
	stack []int
	minMaxStack []node
}

func NewMinMaxStack() *MinMaxStack {
	// Write your code here.
	return &MinMaxStack{}
}

func (stack *MinMaxStack) Peek() int {
	// Write your code here.
	return stack.stack[len(stack.stack)-1]
}

func (stack *MinMaxStack) Pop() int {
	// Write your code here.
	popped := stack.stack[len(stack.stack)-1]
	stack.stack = stack.stack[:len(stack.stack)-1]
	stack.minMaxStack = stack.minMaxStack[:len(stack.minMaxStack)-1]
	return popped
}

func (stack *MinMaxStack) Push(number int) int {
	// Write your code here.
	// want to update min and max as we go 
	if len(stack.stack) == 0 {
		stack.stack = append(stack.stack, number)
		node := node{min: number, max: number}
		stack.minMaxStack = append(stack.minMaxStack, node)
	} else {
		minNode := min(stack.GetMin(), number)
		maxNode := max(stack.GetMax(), number)
		node := node{min: minNode, max: maxNode}
		stack.stack = append(stack.stack, number)
		stack.minMaxStack = append(stack.minMaxStack, node)
	}
	return number
	
}

func (stack *MinMaxStack) GetMin() int {
	// Write your code here.
	return stack.minMaxStack[len(stack.minMaxStack)-1].min
}

func (stack *MinMaxStack) GetMax() int {
	// Write your code here.
	return stack.minMaxStack[len(stack.minMaxStack)-1].max
}


func max(a int, b int) int {
	if a > b {
		return a 
	} else {
		return b 
	}
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}



