class Solution:
    def climbStairs(self, n: int) -> int:
        tot = 0
        a, b = 1, 0
        for _ in range(n):
            a, b = (a + b) ,a
        return a

        
        