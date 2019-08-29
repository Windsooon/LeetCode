class Solution:
    def minMoves(self, nums):
        return sum(nums) - min(nums) * len(nums)

s = Solution()
print(s.minMoves([1,2, 3]))
