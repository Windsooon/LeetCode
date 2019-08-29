import collections

class Solution:
    def findAnagrams(self, s: str, p: str):
        if not s or len(s) < len(p):
            return []
        ans = []
        current_dic = self.expected_sum(s, len(p))
        expected_dic = self.expected_sum(p, len(p))
        if current_dic == expected_dic:
            ans.append(0)
        for i in range(1, len(s)-len(p)+1):
            current_dic[s[i-1]] -= 1
            if current_dic[s[i-1]] == 0:
                del current_dic[s[i-1]]
            current_dic[s[i+len(p)-1]] += 1
            if current_dic == expected_dic:
                ans.append(i)
        return ans

    def expected_sum(self, input, length):
        dic = collections.defaultdict(int)
        for i in range(length):
            dic[input[i]] += 1
        return dic





s = Solution()
str = "abab"
p = "ab"
print(s.findAnagrams(str, p))
