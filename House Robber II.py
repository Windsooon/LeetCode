class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.base_rob(nums[:-1]), self.base_rob(nums[1:]))

    def base_rob(self, nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last+i, now)
        return now


s = Solution()
print(s.rob([1,2,3,1]))
