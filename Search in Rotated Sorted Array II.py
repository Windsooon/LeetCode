class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left] == nums[right]:
                left += 1
            else:
                if nums[mid] > target:
                    if target <= nums[right] and nums[mid] > nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target > nums[right] and nums[mid] <= nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return False

s = Solution()
nums = [3,1,1]
target = 3
print(s.search(nums, target))
