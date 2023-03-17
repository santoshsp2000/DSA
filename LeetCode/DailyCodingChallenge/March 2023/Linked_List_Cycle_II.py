# 142. Linked List Cycle II
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        fst, slw = head, head

        while fst.next and fst.next.next:
            fst = fst.next.next
            slw = slw.next
            if fst == slw:
                break
        else:
            return
        fst = head
        while fst != slw:
            fst = fst.next
            slw = slw.next

        return slw