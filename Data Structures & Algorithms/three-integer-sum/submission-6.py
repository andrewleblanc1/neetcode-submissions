class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #basis of this algorithm, first sort 
        # then iterate through list, and treat like 2 sum
        # except make sure to count for duplicates
        # we count for duplicates by skipping them on left most
        # variable
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            l , r = i + 1, len(nums) - 1
            while r > l:
                
                total = nums[i] + nums[r] + nums[l]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l], nums[r]])
                    l += 1
                    while l < (len(nums) - 1) and nums[l] == nums[l -1]:
                        l += 1
        return res
                

        