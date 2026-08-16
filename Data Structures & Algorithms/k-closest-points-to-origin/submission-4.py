import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kPoints = []
        for point in points:  
            pointTotal = (point[0] ** 2) + (point[1] ** 2)
            if len(kPoints) == k: 
                if kPoints[0][0] > pointTotal:
                    heapq.heappop_max(kPoints)
                    heapq.heappush_max(kPoints, [pointTotal, point[0], point[1]])
                    continue
                else:
                    continue
            else:
                heapq.heappush_max(kPoints, [pointTotal, point[0], point[1]])
        ans = []
        for point in kPoints:
            ans.append((point[1],point[2]))
        return ans


        