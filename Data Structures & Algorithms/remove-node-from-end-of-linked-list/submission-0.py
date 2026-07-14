# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = step = head

        i = 0
        while i < n:
            step = step.next
            i += 1
        prev = None
        new = dummy.next
        if step is None:
            head = head.next
            dummy = None
            return head
        while step is not None:
            step = step.next
            prev = dummy
            dummy = dummy.next
            new = new.next
        prev.next = new
        dummy = None
        return head



        