# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is not None and q is None:
            return False
        if q is not None and p is None:
            return False
        if p.val != q.val:
            return False
        lvp = 0
        rvp = 0
        lvq = 0
        rvq = 0
        if p.left is None:
            lvp = -101
        else:
            lvp = p.left.val
        if p.right is None:
            rvp = -101
        else:
            rvp = p.right.val
        if q.left is None:
            lvq = -101
        else:
            lvq = q.left.val
        if q.right is None:
            rvq = -101
        else:
            rvq = q.right.val
        if lvp != lvq or rvp != rvq:
            return False
        else:
            i = self.isSameTree(p.left,q.left)
            j = self.isSameTree(p.right,q.right)
            return (i and j)
        
    
        