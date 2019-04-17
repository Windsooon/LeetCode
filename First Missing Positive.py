class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1


s = Solution()
print(s.firstMissingPositive([2]))
print(s.firstMissingPositive([3,4,-1,1]))
