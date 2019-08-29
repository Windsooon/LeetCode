import collections

class Solution:
    def findLHS(self, nums):
        ans = 0
        counter = collections.Counter(nums)
        for c in counter:
            if c+1 in counter:
                ans = max(ans, count[c] + count[c+1])
        return ans
