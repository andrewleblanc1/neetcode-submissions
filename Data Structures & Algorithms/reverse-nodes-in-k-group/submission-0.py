# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        j = 0
        while curr is not None and j < k:
            j += 1
            curr = curr.next
        if j == k:
            curr = head
            prev = None
            for i in range(k):
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            head.next = self.reverseKGroup(curr, k)
            return prev
        else:
            return head
            



            


        
                


        

        