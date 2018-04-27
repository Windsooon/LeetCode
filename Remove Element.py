class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [n for n in nums if n != val]
        return len(nums), nums


s = Solution()
print(s.removeElement([3, 3], 3))
