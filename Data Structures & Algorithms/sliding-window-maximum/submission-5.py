import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            ans = []
            ans.append(max(nums))
            return ans
        has = {} # {value : index}
        h = [] # heap queue
        i = j = 0
        ans = []
        # first loop to set j to k and create initial window

        while j < k - 1:
            num = nums[j] * -1
            heapq.heappush(h, num)
            has.update({num: j})
            j += 1
        # sliding window, tracking window size by making sure the index of
        # the popped value is greater than or equal to i, if not, heappop
        # until this is true
        while j < len(nums):
            num = nums[j] * -1
            heapq.heappush(h, num)
            has.update({num: j})
            curr = h[0]
            while has.get(curr) < i:
                heapq.heappop(h)
                curr = h[0]
            curr = curr * -1
            ans.append(curr)
            j += 1
            i += 1
        return ans
            




        