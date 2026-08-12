class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        area = 0
        for i , h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                curr = stack.pop()
                width = i - curr[0]
                height = curr[1]
                area = width * height
                res = max(area, res)
                index = curr[0]
            stack.append([index,h])
        if stack:
            for column in stack:
                width = len(heights) - column[0]
                height = column[1]
                area = width * height
                res = max(area, res)
        return res
        