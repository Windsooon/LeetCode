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


s = Solution()
S = "ACBECDEBANC"
T = "ABC"
print(s.minWindow(S, T))
