class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if (num - 1) in nums:
                continue
            i = 1
            num += 1
            while num in nums:
                i += 1
                num += 1
            res = max(res, i)
        return res
        