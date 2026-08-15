import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for x in range(len(stones)):
            curr = stones[x]
            stones[x] = curr * -1
        print(stones)
        heapq.heapify(stones)
        while len(stones) > 1:
            
            i = heapq.heappop(stones)
            j = heapq.heappop(stones)
            if i == j:
                continue
            elif i < j:
                i = i - j
                heapq.heappush(stones, i)
            else:
                j = j - i
                heapq.heappush(stones, j)
        
        if len(stones) == 0:
            return 0
        return(stones[0] * -1)



        