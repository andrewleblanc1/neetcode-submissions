# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midPoint
        ans = listOne = head 
        ##protect small lists
        if (head.next is None) or (head.next.next is None):
            return
        oneStep = head
        twoStep = head.next
        while (twoStep is not None) and (twoStep.next is not None):
            oneStep = oneStep.next
            twoStep = twoStep.next.next
        temp = oneStep.next
        oneStep.next = None
        oneStep = temp
        #reverseList at oneStep
        prev = None
        while True:
            new = oneStep.next
            oneStep.next = prev
            prev = oneStep
            if new == None:
                break
            oneStep = new     
        # merge both list
        temp = listOne.next
        while oneStep is not None:
            listOne.next = oneStep
            oneStep = oneStep.next
            listOne = listOne.next
            if temp is None:
                break
            listOne.next = temp
            listOne = listOne.next
            temp = temp.next
        listOne.next = None  
        return
        

            
        


        
        
        
        