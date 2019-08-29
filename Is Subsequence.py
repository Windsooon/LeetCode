import collections

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if set(s) - set(t):
            return False
        dic = collections.defaultdict(list)
        minimal = 0
        for i in range(len(t)):
            dic[t[i]].append(i)
        for i in range(len(s)):
            left = self.search(dic[s[i]], minimal)
            if left == len(dic[s[i]]):
                return False
            else:
                minimal = dic[s[i]][left] + 1
        return True

    def search(self, lst, minimal):
        left, right = 0, len(lst)
        while left < right:
            mid = (left + right) // 2
            if lst[mid] < minimal:
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
fir = "acb"
sec = "ahbgdc"
assert s.isSubsequence(fir, sec) is False
fir = "abc"
sec = "ahbgdc"
assert s.isSubsequence(fir, sec) is True
