class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left < len(nums) and nums[left] == target:
            return left
        return -1

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

nums = list(range(100000000))
target = 9
s = Solution()
s.search(nums, target) == 10
