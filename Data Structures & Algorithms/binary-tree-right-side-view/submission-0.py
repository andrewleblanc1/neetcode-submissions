# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        arr = []
        queue = deque()
        queue.append(root)
        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            arr.append(curr)
        ans = []
        for array in arr:
            ans.append(array[len(array) - 1].val)
        return ans
        

        