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

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        dic = collections.defaultdict(int)
        for s_t in t:
            dic[s_t] += 1
        need = len(t)
        up, down, ans = 0, 0, ''
        while up < len(s):
            # ADOBECODEBANC
            if s[up] not in dic:
                up += 1
                continue
            else:
                if dic[s[up]] > 0:
                    need -= 1
                dic[s[up]] -= 1
                while need == 0:
                    if ans == '' or up - down < len(ans):
                        ans = s[down:up+1]
                    if s[down] in dic:
                        dic[s[down]] += 1
                        if dic[s[down]] == 1:
                            need += 1
                    down += 1
                up += 1
        return ans

s = Solution()
S = "aa"
T = "aa"
print(s.minWindow(S, T))
