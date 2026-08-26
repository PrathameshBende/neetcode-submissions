# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node, biggestSoFar):
            if node is None:
                return 0
            
            good = 1 if node.val >= biggestSoFar else 0

            biggestSoFar = max(biggestSoFar, node.val)

            good += dfs(node.left, biggestSoFar)
            good += dfs(node.right, biggestSoFar)

            return good

        return dfs(root, root.val) 