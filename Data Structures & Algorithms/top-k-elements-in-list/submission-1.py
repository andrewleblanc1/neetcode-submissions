class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        flip = {}
        heap = []
        res = []
        for num in nums:
            if has.get(num) is None:
                has.update({num: 1})
            else:
                curr = has.get(num)
                curr += 1
                has.update({num:curr})
        for key, val in has.items():
            if flip.get(val) is None:
                flip.update({val:[key]})
                heapq.heappush_max(heap, val)
            else:
                curr = flip.get(val)
                curr.append(key)
                flip.update({val:curr})
        i = 0
        while i < k:
            maxi = heapq.heappop_max(heap)
            curr = flip.get(maxi)
            while i < k and len(curr) > 0:
                res.append(curr.pop())
                i += 1
        return res

                

        
        

        