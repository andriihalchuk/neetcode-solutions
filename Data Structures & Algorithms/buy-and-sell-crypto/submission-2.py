class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPrice = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
                r += 1
            else:
                maxPrice = max(maxPrice, prices[r] - prices[l])
                r += 1

        return maxPrice
