class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        r_len = min(steps+1, arrLen)
        dp = [[0] * r_len for i in range(steps+1)]
        dp[0][0] = 1
        for i in range(1, steps+1):
            for j in range(r_len):
                if i-1 >= 0 and j-1 >= 0:
                    dp[i][j] += dp[i-1][j-1]
                if i-1 >= 0 and j+1 < r_len:
                    dp[i][j] += dp[i-1][j+1]
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
        return dp[-1][0] % (10**9 + 7)

s = Solution()
s.numWays(430, 148488)
