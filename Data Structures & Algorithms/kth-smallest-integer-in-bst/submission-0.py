# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    def kthSmallest(self, root: Optional[Treenode], k: int) -> int:
        
        if root is None:
            return -1
        if self.count == k:
            return root.val

        if root.left is None and root.right is None:
            self.count += 1
            if self.count == k:
                return root.val
            return -1

        left = self.kthSmallest(root.left, k)
        if left is not -1:
            return left
        
        self.count += 1
        if self.count == k:
            return root.val
        right = self.kthSmallest(root.right, k)
        return right
            
            


