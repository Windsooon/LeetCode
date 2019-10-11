import collections

class Solution:
    def findAnagrams(self, s: str, p: str):
        if not s:
            return []
        ans = []
        need_dict = collections.defaultdict(int)
        for i in range(len(p)):
            need_dict[p[i]] += 1
        need = len(p)
        for i in range(len(s)):
            if i - len(p) >= 0:
                need_dict[s[i-len(p)]] += 1
                if need_dict[s[i-len(p)]] > 0:
                    need += 1
            need_dict[s[i]] -= 1
            if need_dict[s[i]] >= 0:
                need -= 1
            if need == 0:
                ans.append(i-len(p)+1)
        return ans





s = Solution()
str = "baa"
p = "aa"
print(s.findAnagrams(str, p))
