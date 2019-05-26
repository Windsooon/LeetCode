class Solution:
    def findMin(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                right -= 1
        return nums[left]

s = Solution()
assert s.findMin([1,3,5]) == 1
assert s.findMin([2,2,2,0,1]) == 0
assert s.findMin([1,0,1,1,1]) == 0
assert s.findMin([1,1,1,0,1]) == 0
assert s.findMin([2,4,6,0,1]) == 0
