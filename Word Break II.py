class Solution:
    def wordBreak(self, s, wordDict):
        self.wordDict = wordDict
        self.dic = {}
        result = self.recu(s)
        lst = []
        for r in result:
            lst.append(' '.join(r))
        return lst

    def recu(self, s):
        if not s:
            return [[]]
        elif s in self.dic:
            return self.dic[s]
        result = []
        for i in range(1, len(s)+1):
            if s[:i] in self.wordDict:
                for k in self.recu(s[i:]):
                    result.append([s[:i]] + k)
        self.dic[s] = result
        return result


s = Solution()
print(s.wordBreak('applepen', ["abc"]))
print(s.wordBreak('applepen', ["apple", "pen", "applep", "en"]))
print(s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))
