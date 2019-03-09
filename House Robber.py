class Solution:
    def rob(self, nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
# []
# [1]
# [1, 2]
# [1, 2, 4]
# [4, 1, 2, 4]
s = Solution()
assert s.rob([]) == 0
assert s.rob([2, 1, 1, 2]) == 4
assert s.rob([2, 7, 9, 3, 1]) == 12
