class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid] or target == nums[left] or target == nums[right]:
                return True
            if nums[left] < target < nums[mid]:
                right = mid - 1
            elif nums[right] > target > nums[mid]:
                left = mid + 1
            else:
                right -= 1
        return False

s = Solution()
nums = [2,5,6,0,0,1,2]; target = 0
print(s.search(nums, target))
nums = [2,5,6,0,0,1,2]; target = 3
print(s.search(nums, target))
nums = [1,0,1,1,1,1,1]; target = 0
print(s.search(nums, target))
nums = [1,0,1,1,1,1,1]; target = 5
print(s.search(nums, target))
nums = [1,1,1,1,1,0,1]; target = 0
print(s.search(nums, target))
nums = [1,1,1,1,1,0,1]; target = 2
print(s.search(nums, target))
nums = [1,1,1,1,1,0]; target = 0
print(s.search(nums, target))
