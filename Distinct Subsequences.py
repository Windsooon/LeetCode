class Solution:
    def numDistinct(self, s, t):
        l1, l2 = len(s)+1, len(t)+1
        cur = [0] * l2
        cur[0] = 1
        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        return cur[-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        dp = [[0] * len(s) for i in range(len(t))]
        for i in range(len(s)):
            if s[i] == t[0]:
                dp[0][i] = dp[0][i-1] + 1
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(1, len(t)):
            for j in range(i, len(s)):
                if t[i] == s[j]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]


s = Solution()
print(s.numDistinct('rabbbit', 'rabbit'))
print(s.numDistinct('babgbag', 'bag'))
