class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i+1), res, key=len)
        return res

    def helper(self, s, a, b):
        while a >= 0 and b < len(s) and s[a] == s[b]:
            a -= 1
            b += 1
        return s[a+1:b]

class Solution:
    def longestPalindrome(self, s):
        if not s:
            return 0
        longest = s[0]
        dp = [[False] * len(s) for i in range(len(s))]
        for i in range(len(s)-1):
            dp[i][i] = True
            if s[i] == s[i+1]:
                longest = s[i:i+2]
                dp[i][i+1] = True
        dp[-1][-1] = True
        for i in range(len(s)-3, -1, -1):
            for j in range(len(s)-1, i, -1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if (j-i) + 1 > len(longest):
                        longest = s[i:j+1]
        return longest



s = Solution()
print(s.longestPalindrome('bb'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('babad'))
