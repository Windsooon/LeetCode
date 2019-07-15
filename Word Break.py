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

class Solution:
    def wordBreak(self, s, wordDict):
        # DP[i:j] = DP[i:k] + word_in_list(k:j)
        DP = [False] * (len(s)+1)
        DP[0] = True
        for j in range(1, len(DP)):
            for k in range(j):
                if DP[k] and (s[k:j] in wordDict or not s[k:j]):
                    DP[j] = True
        return DP[-1]


s = Solution()
assert s.wordBreak('applepen', ["apple", "pen"]) is True
assert s.wordBreak('applena', ["apple", "applena"]) is True
assert s.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]) is False
assert s.wordBreak('leetcode', ['leet', 'code']) is True
assert s.wordBreak('bb', ["a", "b", 'bbb', 'bbbb']) is True
assert s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) is False
