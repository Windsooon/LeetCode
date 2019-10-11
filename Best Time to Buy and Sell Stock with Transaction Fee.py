class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        # [1, 3, 2, 8]
        #     ^
        # dp[i][hold] = max(dp[i-1][hold], dp[i-1][no] - prices[i] - fee)
        # dp[i][no] = max(dp[i-1][no], dp[i-1][hold] + prices[i] - fee)
        if len(prices) < 2:
            return 0
        dp = [[0]*2 for i in range(len(prices))]
        dp[0][1] = -prices[0] - fee
        for j in range(1, len(prices)):
            dp[j][1] = max(dp[j-1][1], dp[j-1][0] - prices[j] - fee)
            dp[j][0] = max(dp[j-1][0], dp[j-1][1] + prices[j])
        print(dp)
        return dp[-1][0]
                
        
s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))
