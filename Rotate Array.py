class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = nums[-k:] + nums[0:-k]
        print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
s = Solution()
print(s.rotate(nums, k))
