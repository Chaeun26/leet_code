class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        debt=cash=0
        
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                cash+=prices[i+1]-prices[i]
                
        return cash

