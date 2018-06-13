# len < 3 -> None
# [1,2,3,1] -> 2
# [1,2,1,3,5,6,4] -> 1 or 5
# logarithmic complexity

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return
        left, right = 0, len(nums)
        while (right - left) > 1:
            mid = (left+right)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif 
