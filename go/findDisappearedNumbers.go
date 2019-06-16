func findDisappearedNumbers(nums []int) []int {
    if len(nums) == 0 {
        return nil
    }
    unique := make(map[int]int)
    disappeared := make([]int,0)
    for _, val := range nums {
        unique[val]++
    }
    smallest := 1
    for smallest <= len(nums) {
        if _, ok := unique[smallest]; !ok {
            disappeared = append(disappeared, smallest)
        }
        smallest++
    }
    return disappeared
}
