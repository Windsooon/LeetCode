class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(nums, original, target):
            '''
            :type nums: List[int]
            :type original: int
            :type target: int
            '''
            nums[original], nums[target] = nums[target], nums[original]

        if not nums:
            return 1

        for i in range(len(nums)):
            while (nums[i] > 0 and nums[i] != i+1 and nums[i] < len(nums) and nums[nums[i]-1] != nums[i]):
                swap(nums, i, nums[i]-1)

        for k, v in enumerate(nums):
            if v != k+1:
                return k+1

        return len(nums) + 1

nums = [1, 1]
s = Solution()
print(s.firstMissingPositive(nums))
