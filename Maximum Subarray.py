class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_end, max_sum = nums[0], nums[0]
        for i in nums[1:]:
            max_end = max(i, max_end+i)
            max_sum = max(max_end, max_sum)
        return max_sum

s = Solution()
print(s.maxSubArray([1]))
