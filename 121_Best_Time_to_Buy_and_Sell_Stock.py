class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = float('inf')
        
        for price in prices:
            if price < minimum:
                minimum = price
            elif price - minimum > profit:
                profit = price - minimum

        return profit
