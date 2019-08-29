class Solution:
    def countSubstrings(self, s):
        if s == '': return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        breakpoint()
        for r in range(len(s)-1, -1, -1):
            for c in range(r+1, len(s)):
                if c == r+1:
                    dp[r][c] = 1 if s[r]==s[c] else 0
                else:
                    dp[r][c] = 1 if s[r]==s[c] and dp[r+1][c-1]==1 else 0
        return sum([sum(row) for row in dp])



str = 'ababc'
s = Solution()
s.countSubstrings(str)
