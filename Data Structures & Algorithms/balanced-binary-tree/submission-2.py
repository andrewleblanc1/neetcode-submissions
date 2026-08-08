# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]) -> bool:
            if node is None:
                return 0
            hL = check(node.left)
            if hL == -1:
                return -1
            rL = check(node.right)
            if rL == -1:
                return -1
            if hL + 1 == rL:
                return rL + 1
            elif rL + 1 == hL:
                return hL + 1
            elif rL == hL:
                return hL + 1
            else:
                return -1
        if check(root) != -1:
            return True
        else:
            return False
    
        
        

       
        