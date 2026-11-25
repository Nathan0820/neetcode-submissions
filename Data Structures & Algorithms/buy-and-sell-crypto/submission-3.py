class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low_buy = prices[0]
        for price in prices:
            res = max(res, price - low_buy)
            low_buy = min(low_buy, price)
        return res
