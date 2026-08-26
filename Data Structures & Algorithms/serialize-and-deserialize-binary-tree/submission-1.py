# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        q = deque([root])
        s = ""
        while q:
            curr = q.popleft()
            if curr is None:
                s += "N#"
                continue

            s += f"{curr.val}#"
            q.append(curr.left)
            q.append(curr.right)
        print(s)
        return s

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = []
        i = s.inde# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        q = deque([root])
        s = ""
        while q:
            curr = q.popleft()
            if curr is None:
                s += "N#"
                continue

            s += f"{curr.val}#"
            q.append(curr.left)
            q.append(curr.right)
        print(s)
        return s

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        q = deque([])
        values = data.split('#')
        i = 0
        root = TreeNode(values[i])
        i += 1
        q.append(root)
        while q:
            curr = q.popleft()
            if values[i] == 'N':
                curr.left = None
                i += 1
            else:
                curr.left = TreeNode(values[i])
                i += 1
                q.append(curr.left)

            if values[i] == 'N':
                curr.right = None
                i += 1
            else:
                curr.right = TreeNode(values[i])
                i += 1
                q.append(curr.right)
            print(i)
        return root
