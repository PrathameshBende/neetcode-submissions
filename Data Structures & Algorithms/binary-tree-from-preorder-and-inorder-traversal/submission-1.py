# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    preid = 0
    pre = []
    hashmap = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre = preorder

        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i
        return self.dfs(0, len(inorder) - 1)

    def dfs(self, start, end):
        if start > end:
            return None

        curr = TreeNode(self.pre[self.preid])
        self.preid += 1
        idx = self.hashmap.get(curr.val)
        curr.left = self.dfs(start, idx - 1)
        curr.right = self.dfs(idx + 1, end)

        return curr
