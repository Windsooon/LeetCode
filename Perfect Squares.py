class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        sq = [i**2 for i in range(1, int(n**0.5)+1)]
        for i in range(n+1):
            # dp[0] = 1
            # dp[1] = 1
            # dp[4] = 1
            for j in sq:
                if j > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i-j])
        return dp[-1]
s = Solution()
print(s.numSquares(1692))
