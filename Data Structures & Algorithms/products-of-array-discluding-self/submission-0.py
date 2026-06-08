class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for num in nums:
            total *= num
        ans = [0] * len(nums)
        for i in range(len(ans)):
            if nums[i] == 0:
                numsCopy = nums[:]
                numsCopy.pop(i)
                tot = 1
                for num in numsCopy:
                    tot *= num
                ans[i] = tot
            else:
                ans[i] = total // nums[i]
        return ans