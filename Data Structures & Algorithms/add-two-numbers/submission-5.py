# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        nextt = None
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1Val = 0
            else:
                l1Val = l1.val
            if l2 is None:
                l2Val = 0
            else:
                l2Val = l2.val
            currVal = l1Val + l2Val + carry
            carry = 0
            if currVal >= 10:
                currVal = currVal % 10
                carry = 1
            curr.val = currVal
            nextt = ListNode()
            curr.next = nextt
            prev = curr
            curr = nextt
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry == 1:
            curr.val = 1
        else:
            prev.next = None
        return head
            

            
        
        

            
            
            
        


        

        