class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        ans = 0
        # convert string to int:
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    if matrix[i][j] == '1':
                        dp[i][j] = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        ans = max(max(row) for row in dp)
        return ans**2

s = Solution()
matrix = [["1"]]
print(s.maximalSquare(matrix))
