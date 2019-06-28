import "container/heap"

type Interval struct {
  start int
  end int 
}
  
type ByInterval []Interval
type ByIntervalHeap []int
  
// sorting intervals interface 
func (a ByInterval) Len() int { return len(a) }
func (a ByInterval) Less(i, j int) bool { return a[i].start < a[j].start }
func (a ByInterval) Swap(i, j int) { a[i], a[j] = a[j], a[i] }

// initializing min heap
func (h ByIntervalHeap) Len() int { return len(h) }
func (h ByIntervalHeap) Min() int { return h[0] }
func (h ByIntervalHeap) Less(i, j int) bool {return h[i] < h[j] }
func (h ByIntervalHeap) Swap(i, j int)  { h[i], h[j] = h[j], h[i] }
  
func (h *ByIntervalHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *ByIntervalHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minMeetingRooms(intervals [][]int) int {
  if len(intervals) == 0 {
    return 0
  }
  intervalsSorted := make(ByInterval, 0)
  for _, interval := range intervals {
    intervalsSorted = append(intervalsSorted, Interval{start: interval[0], end: interval[1]})
  }
  sort.Sort(ByInterval(intervalsSorted))
  heapIntervals := &ByIntervalHeap{intervalsSorted[0].end}
  heap.Init(heapIntervals)
  for i := 1; i < len(intervalsSorted); i++ {
    if heapIntervals.Min() <= intervalsSorted[i].start {
      heap.Pop(heapIntervals)
    }
    heap.Push(heapIntervals, intervalsSorted[i].end)
  }
  return heapIntervals.Len()
}
