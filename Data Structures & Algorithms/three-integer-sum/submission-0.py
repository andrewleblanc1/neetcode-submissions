class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = []

        for i in range(len(nums)- 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot < 0:
                    j += 1
                elif tot > 0:
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in target:
                        target.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return target

                    

        