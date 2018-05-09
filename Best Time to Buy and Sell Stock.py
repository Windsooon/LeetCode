class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        profit, min_value = 0, prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i]-min_value)
            if i == len(prices)-1:
                break
            if prices[i+1] > prices[i]:
                min_value = min(min_value, prices[i])
        return profit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
