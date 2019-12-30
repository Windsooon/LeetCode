class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if k == 1:
            return self.calculate(0, len(s)-1, s)

        dp = [[float('inf')] * k for i in range(len(s)+1)]

        for i in range(len(s)):
            dp[i][0] = self.calculate(i, len(s)-1, s)
        for i in range(k):
            dp[-1][i] = 0
        for i in range(len(s)-2, -1, -1):
            for j in range(1, k):
                for row in range(i, len(s)):
                    dp[i][j] = min(dp[i][j], self.calculate(i, row, s) + dp[row+1][j-1])
        return dp[0][-1]

    def calculate(self, start, end, s):
        count = 0
        while start < end:
            if s[start] != s[end]:
                count += 1
            start += 1
            end -= 1
        return count

so = Solution()
s = "ifamcbfrbprx"
k = 5
print(so.palindromePartition(s, k))

# [[0, 1, 1, 2, 2]
#  [1, 1, 2, 2, 3]
#  [1, 2, 2, 3, 2]
#  [2, 2, 3, 2, 2]
#  [2, 3, 2, 2, 1]
#  [3, 3, 2, 1, 1]
#  [3, 2, 1, 1, 1]
#  [3, 1, 1, 1, 0]
#  [4, 1, 1, 0, 0]
#  [5, 1, 0, 0, 0]
#  [5, 0, 0, 0, 0]
#  [0, 0, 0, 0, 0]]
