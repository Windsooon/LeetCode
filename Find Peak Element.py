# len < 3 -> None
# [1,2,3,1] -> 2
# [1,2,1,3,5,6,4] -> 1 or 5
# logarithmic complexity

class Solution:
    def findPeakElement(self, nums):
        if not nums:
            return
        l, r = 0, len(nums)-1
        # breakpoint()
        while l < r:
            mid = (r+l)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
assert s.findPeakElement([1,2,3,1]) == 2
assert s.findPeakElement([1,2,1,3,5,6,4]) == 5
assert s.findPeakElement([1,6,5,7,8]) == 4
