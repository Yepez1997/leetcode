func rangeSumBST(root *TreeNode, L int, R int) int {
    treeSum := 0
    dfs(root, L, R, &treeSum)
    return treeSum
    
}

func dfs(root *TreeNode, L int, R int, total *int) {
    if (root != nil) {
        if (root.Val >= L && root.Val <= R) {
           *total += root.Val
        }
        if (L < root.Val) {
            dfs(root.Left, L, R, total)
        }
        if (R > root.Val) {
            dfs(root.Right, L, R, total)
        }
    }
}
