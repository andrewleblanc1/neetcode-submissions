# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = float('-inf')
        stack = [[root,maxx]]
        count = 0

        while stack:
            curr = stack.pop()
            node = curr[0]
            maximum = curr[1]
            if node:
                if node.val >= maximum:
                    count += 1
                    maximum = node.val
                stack.append([node.left,maximum])
                stack.append([node.right,maximum])



        return count

        


        