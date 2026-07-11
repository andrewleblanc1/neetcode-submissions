import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        l = 1
        r = upperBound
        m = ((r + l) // 2)
        while l < r:
            m = ((r + l) // 2)
            k = 0
            for p in piles:
                k += math.ceil(p/m)
            if k <= h:
                r = m
            else:
                l = m + 1
        return l

        