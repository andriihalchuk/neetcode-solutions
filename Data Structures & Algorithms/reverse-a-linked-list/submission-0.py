# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, val = None, head

        while val:
            nex = val.next
            val.next = prev
            prev = val
            val = nex
        return prev
            