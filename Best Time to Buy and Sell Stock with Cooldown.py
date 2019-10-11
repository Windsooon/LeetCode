class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [[0] * len(prices) for i in range(2)]
        dp[1]
        for i in range(1, len(prices)):
            # not sell
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            for j in range(i-2):
                dp[1][i] = max(dp[1][i], max(dp[1][j], dp[0][j])+prices[i]-prices[j+2])
            # sell
        print(dp)
        return max(dp[0][-1], dp[1][-1])

s = Solution()
print(s.maxProfit([1,2,3,5,29]))
