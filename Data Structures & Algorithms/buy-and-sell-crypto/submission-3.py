class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        
        for i in range(1, len(prices)):
            profit = prices[i] - min(prices[0:i])
            profits.append(profit)
        
        return max(profits) if max(profits) > 0 else 0
            

