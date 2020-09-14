# Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=float("inf")
        maxProfit=0
        
        for i in range(len(prices)):
            if(prices[i]<minPrice):
                minPrice=prices[i]
            else:
                maxProfit=max(maxProfit,prices[i]-minPrice)
    
        return maxProfit