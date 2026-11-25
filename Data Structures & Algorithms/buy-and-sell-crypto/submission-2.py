class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low_buy = float('inf')
        for price in prices:
            if price < low_buy:
                low_buy = price
            else:
                profit = price - low_buy
                res = max(res, profit)
        return res
