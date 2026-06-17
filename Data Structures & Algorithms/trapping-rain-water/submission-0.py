class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxR = 0
        maxL = 0
        trapped = 0
        ans = 0
        for i in range(len(height)):
            maxLeft[i] = maxL
            maxL = max(maxL, height[i])

        for j in range(len(height) - 1, -1, -1):
            maxRight[j] = maxR
            maxR = max(maxR, height[j])
        for i in range(len(height)):
            trap = min(maxLeft[i], maxRight[i]) - height[i]
            trapped = max(0, trap)
            ans += trapped
        return ans
        