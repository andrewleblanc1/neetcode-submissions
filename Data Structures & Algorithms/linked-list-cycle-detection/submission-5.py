# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None) or (head.next is None) or (head.next.next is None):
            return False
        oneStep = head.next
        twoStep = head.next.next
        while oneStep is not None and twoStep is not None:
            if oneStep == twoStep:
                return True
            oneStep = oneStep.next
            twoStep = twoStep.next
            if twoStep is None:
                return False
            else:
                twoStep = twoStep.next

        return False

        