func maximumProduct(nums []int) int {
  sort.Ints(nums)
  return max((nums[0]*nums[1]*nums[len(nums)-1]), (nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3]))
}

func max(a, b int) int {
  if a >= b {
    return a
  }
  return b
}
