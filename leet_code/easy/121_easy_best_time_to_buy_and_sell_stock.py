#121. Best Time to Buy and Sell Stock
#Input: prices = [7,1,5,3,6,4]
#Output: 5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_min = prices[0]
        for price in prices[1:]:
            if price < cur_min:
                cur_min = price
            if price - cur_min > profit:
                profit = price - cur_min
        return profit
