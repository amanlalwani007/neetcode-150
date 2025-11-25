# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 99999
        maxprofit = 0
        for price in prices:
            maxprofit = max(maxprofit, price - minprice)
            minprice = min(minprice, price)
        return maxprofit
        
    
    
# Approach 1: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)


