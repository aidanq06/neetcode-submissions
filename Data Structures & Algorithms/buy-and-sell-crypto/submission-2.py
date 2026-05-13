class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can't sort since prices is time sensitive
        
        left = 0
        profit = 0

        for right in range(1,len(prices)):
            if len(prices) == 1: # if the list length is 1, we cant make a profit
                return profit

            profit = max(profit, prices[right] - prices[left])

            if prices[left] > prices[right]:
                left=right

        
        return profit