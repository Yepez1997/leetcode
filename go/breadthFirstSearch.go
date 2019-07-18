package program

// Do not edit the class below except
// for the breadthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
type Node struct {
	Name     string
	Children []*Node
}

func (n *Node) BreadthFirstSearch(array []string) []string {
	// Write your code here.
	// add the root to the queue
	queue := []*Node{n}
	for len(queue) != 0 {
		node := queue[0]
		queue = queue[1:]
		// exploring the current Nodes children
		array = append(array, node.Name)
		for _, child := range node.Children {
			queue = append(queue, child)
		}
	}
	return array

}
