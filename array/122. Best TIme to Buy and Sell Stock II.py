from typing import List 

class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        profit , maxProfit = 0 ,0
        left = 0 
        right = left + 1

        while left < right and right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit += profit
            left = right
            right = left + 1
        return maxProfit 