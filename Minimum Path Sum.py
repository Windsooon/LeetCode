class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 3, 3
        m, n = len(grid), len(grid[0])
        # [1, 3, 1]
        dp = [grid[0][0]] + [0] * (n-1)
        for k in range(1, n):
            dp[k] = dp[k-1] + grid[0][k]
        # dp = [1, 4, 5]
        for i in range(1, m):
            # 0, 1, 2
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j]+grid[i][j], dp[j-1]+grid[i][j])
        return dp[n-1]


lst = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

s = Solution()
print(s.minPathSum(lst))
