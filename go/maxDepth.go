func maxDepth(root *TreeNode) int {
    if (root == nil) {
        return 0
    }
    left := maxDepth(root.Left)
    right := maxDepth(root.Right)
    return 1 + max(left, right)
}

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}
