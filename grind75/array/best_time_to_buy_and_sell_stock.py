"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            elif profit < (prices[right] - prices[left]):
                profit = prices[right] - prices[left]
            right += 1
            
        return profit