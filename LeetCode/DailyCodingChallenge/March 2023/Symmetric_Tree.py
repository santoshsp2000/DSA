# 101. Symmetric Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:

    def check(self, root1, root2):

        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        return root1.val == root2.val and self.check(root1.left, root2.right) and self.check(root1.right, root2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left: return True

        return self.check(root.left, root.right)
