# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        big = float('inf')
        small = -float('inf')
        def dfs(node, big, small):
            if node is None:
                return True

            if small < node.val and node.val < big:
                return dfs(node.left, node.val, small) and dfs(node.right, big, node.val)
            
            else:
                return False
        
        return dfs(root, big, small)

        