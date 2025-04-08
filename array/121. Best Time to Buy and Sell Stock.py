from typing import List;

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        profit , maxProfit = 0, 0

        while left < right and right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit )
                right += 1
            else:
                left = right 
                right = left + 1