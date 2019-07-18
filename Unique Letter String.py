class Solution:
    def uniqueLetterString(self, S):
        if not S:
            return 0
        last = [-1] * 26
        before_last = [-1] * 26
        ans = 0
        dp = 0
        for i in range(len(S)):
            index = ord(S[i]) - ord('A')
            dp = dp + (i-last[index]) - (last[index]-before_last[index])
            ans += dp
            before_last[index] = last[index]
            last[index] = i
        return ans





s = Solution()
S = "ABC"
print(s.uniqueLetterString(S))
