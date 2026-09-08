# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [[root, -float('inf'), float('inf')]]

        while stack:
            curr = stack.pop()
            node, minn, maxx = curr[0], curr[1], curr[2]

            if node:
                if node.val >= maxx or node.val <= minn:
                    return False
                else:
                    stack.append([node.left, minn, node.val])
                    stack.append([node.right, node.val, maxx])
        return True



        
        
        
        