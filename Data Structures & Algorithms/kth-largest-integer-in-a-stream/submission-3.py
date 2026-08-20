import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.length = k
        self.num = []
        for nu in nums:
            if len(self.num) < k:
                heapq.heappush(self.num, nu)
            elif self.num[0] < nu:
                heapq.heappop(self.num)
                heapq.heappush(self.num, nu)
        while len(self.num) < k:
            heapq.heappush(self.num, -1001)
            
        

    def add(self, val: int) -> int:
        heapq.heappush(self.num, val)
        if len(self.num) > self.length:
            heapq.heappop(self.num)
        return self.num[0]
        
