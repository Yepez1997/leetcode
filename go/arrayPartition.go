func arrayPairSum(nums []int) int {
  totalSum := 0; 
  sort.Ints(nums)
  for i, j := 0, 1; i < len(nums) && j < len(nums); i, j = i + 2, j + 2 {
    fmt.Print(nums[i], nums[j])
    minNum := min(nums[i], nums[j])
    totalSum += minNum
  }
  return totalSum
}

func min(a, b int) int {
  if a < b {
    return a 
  }
  return b
}
