class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices) - 1):
            ind = i + 1
            copyPrices = prices[ind:]
            res = max(copyPrices) - prices[i]
            print(res)
            ans = max(ans, res)

        return ans


        