class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)

s = Solution()
assert s.missingNumber([4, 5, 7]) == 6
assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
