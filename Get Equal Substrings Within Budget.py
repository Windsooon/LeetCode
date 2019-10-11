class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        cost = 0
        for i in range(len(s)):
            cost += abs(ord(s[i])-ord(t[i]))
            if cost > maxCost:
                cost -= abs(ord(s[start])-ord(t[start]))
                start += 1
        return i - start + 1

so = Solution()
s = "abcd"
t = "cdef"
maxCost = 3
print(so.equalSubstring(s, t, maxCost))
