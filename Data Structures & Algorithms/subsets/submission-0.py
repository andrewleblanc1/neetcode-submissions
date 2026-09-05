class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []

        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            # include number
            curr.append(nums[i])
            dfs(i + 1)

            # dont include number
            
            curr.pop()
            dfs(i + 1)
        dfs(0)
        return res

        