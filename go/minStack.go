type Node struct {
    min int 
    val int 
    prev *Node
}

type MinStack struct {
    stack []Node
    size int 
}


/** initialize your data structure here. */
func Constructor() MinStack {
  return MinStack{stack: []Node{}, size: 0}
}

func (this *MinStack) Size() int {
  return this.size
}

func (this *MinStack) Push(x int)  {
  if len(this.stack) == 0 {
    node := Node{min: x, val: x, prev: nil}
    this.size++
    this.stack = append(this.stack, node)
  } else {
    prevNode := this.stack[this.size-1]
    node := Node{val: x, prev: &prevNode}
    if x <= prevNode.min {
      // update min value 
      node.min = x  
    } else {
      node.min = prevNode.min
    }
    this.size++
    this.stack = append(this.stack, node)
  }
}


func (this *MinStack) Pop()  {
    //top := this.stack[len(this.stack)-1]
    this.stack = this.stack[:len(this.stack)-1]
    this.size-- 
}


func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1].val
}


func (this *MinStack) GetMin() int {
  // get the min of the top stack
  return this.stack[this.Size()-1].min 
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
