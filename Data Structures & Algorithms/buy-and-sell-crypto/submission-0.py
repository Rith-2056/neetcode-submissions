class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curProfit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                curProfit = prices[j] - prices[i]
                profit = max(curProfit, profit)
        return profit