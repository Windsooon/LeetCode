class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        k = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                k += 1
        return len(nums) - k


s = Solution()
lst = [1, 1, 2]
assert s.removeDuplicates(lst), 2
