from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def inorder(self, node: Optional[TreeNode], ans: List[int]) -> List[int]:
        if not node: return

        if node.left: self.inorder(node.left, ans)

        ans.append(node.val)

        if node.right: self.inorder(node.right, ans)

        return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        return self.inorder(root, ans)
