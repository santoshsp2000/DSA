# 515. Find Largest Value in Each Tree Row
# Leetcode Medium
# Date: 24 October 2023
# TC: O(N)
# SC: O(N)
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        mapp = {}

        if root: que.append((root, 0))

        while que:
            n = len(que)
            for nod in range(n):
                node, lvl = que.popleft()
                if lvl in mapp:
                    if mapp[lvl] < node.val:
                        mapp[lvl] = node.val
                else:
                    mapp[lvl] = node.val
                if node.left:
                    que.append((node.left, lvl + 1))
                if node.right:
                    que.append((node.right, lvl + 1))

        ans = []
        ind = 0
        while ind in mapp:
            ans.append(mapp[ind])
            ind += 1

        return ans
