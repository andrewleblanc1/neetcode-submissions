# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque()
        res = []
        if root:
            stack.append(root)
        while stack:
            curr = []
            for _ in range(len(stack)):
                currNode = stack.popleft()
                curr.append(currNode.val)
                if currNode.left:
                    stack.append(currNode.left)
                if currNode.right:
                    stack.append(currNode.right)
            res.append(curr)
        return res

        
        