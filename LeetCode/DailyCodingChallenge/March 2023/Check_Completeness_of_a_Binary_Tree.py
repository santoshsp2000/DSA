# 958. Check Completeness of a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([root])
        flag = False

        while que:
            n = len(que)
            flag = False

            for i in range(n):
                node = que.popleft()
                if not node:
                    flag = True
                    break
                que.append(node.left)
                que.append(node.right)

            while que and flag:
                val = que.popleft()
                if val: return False

        return True
