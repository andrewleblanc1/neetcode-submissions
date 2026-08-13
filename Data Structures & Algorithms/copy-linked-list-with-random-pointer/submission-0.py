"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        has = {}
        answer = curr = head 
        while head is not None:
            new = Node(head.val)
            has.update({head:new})
            head = head.next
        while curr is not None:
            clone = has.get(curr)
            clone.next = has.get(curr.next)
            clone.random = has.get(curr.random)
            curr = curr.next
        return(has.get(answer))
        
        
