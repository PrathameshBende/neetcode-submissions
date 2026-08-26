# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return [-1001, -1001]
            left = dfs(node.left)
            right = dfs(node.right)

            m = max(node.val, left[0] + node.val, right[0] + node.val)
            mi = max(left[1], right[1], node.val + left[0] + right[0], left[0], right[0])

            return [m, mi]
        res = dfs(root)
        return max(res[0], res[1])
