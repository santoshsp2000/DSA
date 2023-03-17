# 109. Convert Sorted List to Binary Search Tree


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return
        fst, slw = head, head
        prev = head

        while fst and fst.next:
            fst = fst.next.next
            prev = slw
            slw = slw.next

        prev.next = None
        root = TreeNode(slw.val)

        if slw != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slw.next)

        return root
