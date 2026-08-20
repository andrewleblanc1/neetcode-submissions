import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.length, self.num = k, nums
        heapq.heapify(self.num)
        while len(self.num) > k:
            heapq.heappop(self.num)
            
    def add(self, val: int) -> int:
        heapq.heappush(self.num, val)
        if len(self.num) > self.length:
            heapq.heappop(self.num)
        return self.num[0]
        
