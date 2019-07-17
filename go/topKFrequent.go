
import "container/heap"

type weightedElement struct {
  data int
  weight int 
}

type topHeap []weightedElement;

// interface for heap
func (h topHeap) Len() int           { return len(h) }
func (h topHeap) Less(i, j int) bool { return h[i].weight > h[j].weight }
func (h topHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *topHeap) Push(x interface{}) {
	*h = append(*h, x.(weightedElement))
}

func (h *topHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func topKFrequent(nums []int, k int) []int {
  frequencies := make(map[int]int)
  for _, v := range nums {
    frequencies[v]++
  }
  topK := &topHeap{}
  heap.Init(topK)
  // insert all to the priority queue 
  for k, v := range frequencies {
    node := weightedElement{data: k, weight: v}
    heap.Push(topK, node)
  }
  
  results := make([]int,0)
  for k > 0 {
    popped := heap.Pop(topK)
    results = append(results, popped.(weightedElement).data)
    k--
  }
  return results;
  
}
