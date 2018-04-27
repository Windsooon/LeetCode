class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # If the nums is empty or only contain one value
        if len(nums) <= 1:
            return
        # Get the reverse nums
        for i in range(1, len(nums)):
            # Found the first value small than its left side
        nums = nums[::-1]

s = Solution()
# s.nextPermutation([1, 2, 3])
s.nextPermutation([1, 8, 3, 7, 5])
# s.nextPermutation([3, 2, 1])
