# 129. Sum Root to Leaf Numbers


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:

    def find(self, root, summ, s):
        if not root.left and not root.right:
            summ[0] += int(s + str(root.val))
            return

        if root.left:
            self.find(root.left, summ, s + str(root.val))

        if root.right:
            self.find(root.right, summ, s + str(root.val))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = [0]
        self.find(root, summ, '')

        return summ[0]
