# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        leftDia = self.diameterOfBinaryTree(root.left)
        rightDia = self.diameterOfBinaryTree(root.right)
        dep = self.depth(root.left) + self.depth(root.right)
        
        return max(leftDia, rightDia, dep)

    def depth(self, root):
        if root == None:
            return 0
        
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)

        return max(leftDepth, rightDepth) + 1