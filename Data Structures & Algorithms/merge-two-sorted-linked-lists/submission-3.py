# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        x = list1
        prevx = None
        y = list2
        while y is not None:
            if x.val == y.val:
                tempy = y.next
                temp = x.next
                x.next = y
                y.next = temp
                y = tempy
            elif x.val < y.val:
                tempy = y.next
                while (x.next is not None) and x.next.val < y.val:
                    prevx = x
                    x = x.next
                temp = y
                y.next = x.next
                x.next = y
                y = tempy
            elif x.val > y.val:
                temp = y.next
                if prevx is not None:
                    prevx.next = y
                y.next = x
                prevx = y
                y = temp
        if list1.val > list2.val:
            return list2
        else:
            return list1


                    

       




        