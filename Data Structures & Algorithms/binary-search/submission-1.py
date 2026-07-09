class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        m = (r-l) // 2
        while l < r:
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                m = l + (r-l) // 2
            else:
                r = m
                m = l + (r-l) // 2
        return -1
        