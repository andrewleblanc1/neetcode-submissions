import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.length = k
        heapq.heapify(nums)
        self.num = nums
        while len(self.num) > k:
            heapq.heappop(self.num)
        while len(self.num) < k:
            heapq.heappush(self.num, -1001)
            
        

    def add(self, val: int) -> int:
        if self.num[0] < val:
            heapq.heappop(self.num)
            heapq.heappush(self.num, val)
        return self.num[0]
        
