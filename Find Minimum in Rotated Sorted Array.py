class Solution:
    def findMin(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

s = Solution()
assert s.findMin([3,4,5,1,2]) == 1
assert s.findMin([4,5,6,7,0,1,2]) == 0
assert s.findMin([6,0,1,2,3,4,5]) == 0
assert s.findMin([6,0,1]) == 0
