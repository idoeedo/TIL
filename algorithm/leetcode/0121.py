import sys
from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            today = prices[i]
            future = max(prices[i:])
            if future - today > profit:
                profit = future - today

        return profit


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
