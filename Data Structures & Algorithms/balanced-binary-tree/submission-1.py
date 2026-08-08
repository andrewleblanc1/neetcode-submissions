# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            if root.left is None and root.right is None:
                root.height = 1
                return True
            elif root.left is None:
                if root.right.height > 1:
                    return False
                root.height = root.right.height + 1
                return True
            elif root.right is None:
                if root.left.height > 1:
                    return False
                root.height = root.left.height + 1
                return True
            else:
                if root.left.height == root.right.height:
                    root.height = root.left.height + 1
                    return True
                elif root.left.height + 1 == root.right.height:
                    root.height = root.right.height + 1
                    return True
                elif root.right.height + 1 == root.left.height:
                    root.height = root.left.height + 1
                    return True
                else:
                    return False
        else:
            return False

                
        