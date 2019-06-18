func majorityElement(nums []int) int {
    counts := make(map[int]int)
    for _, val := range nums {
        counts[val]++
    }
    var maj int
    for k, v := range counts {
        if v > len(nums)/2 {
            maj = k
        }
    }
    return maj
}
