# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.val == root2.val:
            return self.sameTree(root1.left,root2.left) and self.sameTree(root1.right,root2.right)
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot):
            return True
        elif root.left is not None and root.right is not None:
            return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.left, subRoot))
        elif root.left is None and root.right is not None:
            return self.isSubtree(root.right, subRoot)
        elif root.left is not None and root.right is None:
            return self.isSubtree(root.left, subRoot)
        else:
            return False
            
        