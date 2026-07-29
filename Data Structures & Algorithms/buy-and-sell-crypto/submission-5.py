class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        max = 0
        for i in range(len(prices)):
            price = prices[i]
            if price > prices[r]:
                r = i
            dif = prices[r] - prices[l]
            max = dif  if dif > max else max
            if price < prices[l]:
                l = i
                r = i
        return max
            
