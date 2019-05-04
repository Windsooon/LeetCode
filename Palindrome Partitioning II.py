class Solution:
    def minCut(self, s):
        #aabc
        dp = [[0] * len(s) for i in range(len(s))]
        min_cut = len(s)-1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (j-1 == i or j-1 >= i+1 and dp[i


s = Solution()
print(s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrr"))
