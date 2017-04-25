import collections


class Solution(object):
    def findSubstringInWraproundString(self, p):
        p, d, lo = '0'+p, collections.defaultdict(int), 0
        for hi in range(1, len(p)):
            if p[hi-1]+p[hi] not in 'abcdefghijklmnopqrstuvwxyza':
                lo = 1
            d[p[hi]] = max(d[p[hi]], lo)
            lo += 1
        return sum(d.values())


b = Solution()
print(b.findSubstringInWraproundString('abcdabc'))
