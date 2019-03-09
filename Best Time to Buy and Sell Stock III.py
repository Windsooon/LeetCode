class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0] * len(prices) for i in range(3)]
        for k in range(1, 3):
            min_val = prices[0]
            for i in range(1, len(prices)):
                min_val = min(min_val, prices[i] - dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i] - min_val)
        return dp[2][len(prices) - 1]


s = Solution()
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
