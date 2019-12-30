import collections

class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        p_dic = collections.defaultdict(int)
        s_dic = collections.defaultdict(int)
        for i in range(len(p)):
            p_dic[p[i]] += 1
        for i in range(len(s)):
            if i <= len(p)-1:
                s_dic[s[i]] += 1
            else:
                if s_dic == p_dic:
                    res.append(i-len(p))
                s_dic[s[i]] += 1
                s_dic[s[i-len(p)]] -= 1
                if s_dic[s[i-len(p)]] == 0:
                    del s_dic[s[i-len(p)]]
        return res



s = Solution()
str = "abab"
p = "ab"
print(s.findAnagrams(str, p))
