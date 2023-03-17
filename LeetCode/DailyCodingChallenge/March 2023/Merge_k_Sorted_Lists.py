# 23. Merge k Sorted Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def merge(self, head1, head2):
        start = None
        if head1.val <= head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        start = head

        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next

        if head1:
            head.next = head1

        if head2:
            head.next = head2

        return start

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        i = 0
        while i < n and not lists[i]:
            i += 1
        if i == n: return
        head = lists[i]

        for j in range(i + 1, n):
            if lists[j]:
                if not head:
                    head = lists[j]
                else:
                    head = self.merge(head, lists[j])

        return head