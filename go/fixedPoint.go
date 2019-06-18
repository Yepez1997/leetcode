//Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.
func fixedPoint(A []int) int {
    for i, v := range A {
        if v == i {
            return i
        }
    }
    return -1
}
