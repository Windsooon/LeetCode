class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True] + [False] * len(s)
        true_index = [0]
        for i in range(1, len(dp)):
            for t in true_index:
                if s[t:i] in wordDict:
                    dp[i] = True
                    if i not in true_index:
                        true_index.append(i)
        return dp[-1]


s = Solution()
assert s.wordBreak('applepenapple', ["apple", "pen"]) is True
assert s.wordBreak('applena', ["apple", "applena"]) is True
assert s.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]) is False
assert s.wordBreak('leetcode', ['leet', 'code']) is True
assert s.wordBreak('bb', ["a", "b", 'bbb', 'bbbb']) is True
assert s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) is False
