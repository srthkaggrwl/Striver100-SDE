
class Solution(object):
    def maxProfit(self, prices):
        
        profit = 0
        buying_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < buying_price:
                buying_price = prices[i]

            if profit < prices[i] - buying_price:
                profit = prices[i] - buying_price

        print(profit)            

solution = Solution()
prices =[7,1,5,3,6,4]
solution.maxProfit(prices)