class Solution:
    def numTrees(self, n: int) -> int:
        if n <=2:
            return n
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]

s = Solution()
print(s.numTrees(4))
