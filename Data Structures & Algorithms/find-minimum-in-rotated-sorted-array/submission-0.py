class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (r-l) // 2

        while l < r:
            if nums[m] > nums[r]:
                l = m + 1
                m = ((r - l) // 2) + l
            else:
                r = m 
                m = ((r - l) // 2) + l
        return nums[m]
        
            
        