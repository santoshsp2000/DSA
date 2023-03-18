# 106. Construct Binary Tree from Inorder and Postorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:

    def constructTree(self, inStart, inEnd, inord, postStart, postEnd, postorder):

        if postStart > postEnd or inStart > inEnd: return

        node = TreeNode(postorder[postEnd])
        eleLft = inord[node.val] - inStart
        eleRht = inEnd - inord[node.val]

        node.left = self.constructTree(inStart, inEnd - eleRht - 1, inord, postStart, postEnd - eleRht - 1, postorder)
        node.right = self.constructTree(inStart + eleLft + 1, inEnd, inord, postStart + eleLft, postEnd - 1, postorder)

        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        inord = {}
        n = len(postorder)

        for i in range(n):
            inord[inorder[i]] = i

        return self.constructTree(0, n - 1, inord, 0, n - 1, postorder)
