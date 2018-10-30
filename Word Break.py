class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * len(s)
        for index in range(1, len(s)+1):
            if s[:index] in wordDict: 
                dp[index-1] = True
        for index in range(len(dp)+1):
            for i in range(index):
                if dp[i]:
                    if s[i+1:index] in wordDict:
                        dp[index-1] = True
        return dp[-1]


s = Solution()
assert s.wordBreak('applepenapple', ["apple", "pen"]) is True
assert s.wordBreak('applena', ["apple", "applena"]) is True
assert s.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]) is False
assert s.wordBreak('leetcode', ['leet', 'code']) is True
assert s.wordBreak('bb', ["a", "b", 'bbb', 'bbbb']) is True
assert s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) is False
