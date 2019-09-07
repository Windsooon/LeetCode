import collections

class Solution:
    def minWindow(self, s, t):
        dic, missing = collections.Counter(t), len(t)
        start = 0
        left, right = 0, len(s)
        for i in range(len(s)):
            if dic[s[i]] > 0:
                missing -= 1
            dic[s[i]] -= 1
            if not missing:
                while start < len(s) and dic[s[start]] < 0:
                    dic[s[start]] += 1
                    start += 1
                if i - start < right - left:
                    left, right = start, i
                dic[s[start]] += 1
                start += 1
                missing += 1
        return s[left:right+1]

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = collections.defaultdict(int)
        for i in range(len(t)):
            d[t[i]] += 1
        need = len(t)
        start = end = 0
        min_len = (0, float('inf'))
        while end < len(s):
            if d[s[end]] > 0:
                need -= 1
            d[s[end]] -= 1
            while need == 0:
                if start <= end:
                    if end - start < min_len[1] - min_len[0]:
                        min_len = (start, end)
                d[s[start]] += 1
                if d[s[start]] > 0:
                    need += 1
                start += 1
            end += 1
        return s[min_len[0]:min_len[1]+1]

s = Solution()
S = "ADOBECODEBANC"
T = ""
print(s.minWindow(S, T))
