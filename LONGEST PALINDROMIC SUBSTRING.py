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

b = Solution()
print(b.longestPalindrome('babad'))
