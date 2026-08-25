# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        elif sub is None:
            return True
        if root.val == sub.val and self.isSub(root, sub):
            return True
        else:
            return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)

    def isSub(self, root, sub):
        if root is None and sub is None:
            return True

        if root is None or sub is None:
            return False

        if root.val != sub.val:
            return False
        else:
            return self.isSub(root.left, sub.left) and self.isSub(root.right, sub.right)