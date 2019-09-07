class Solution:
    def searchRange(self, nums, target: int):

        left = self.small_index(0, len(nums)+1, nums, target)
        right = self.large_index(0, len(nums)+1, nums, target)
        return [left, right]

    def small_index(self, left, right, nums, target):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                if nums[mid-1] != target:
                    return mid
                else:
                    right = mid
            else:
                left = mid + 1
        return -1

    def large_index(self, left, right, nums, target):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                if mid == len(nums) or nums[mid+1] != target:
                    return mid
                else:
                    left = mid + 1
            else:
                left = mid + 1
        return -1


s = Solution()
# nums = [5, 7, 7, 8, 8, 10]
nums = [8, 8, 8, 8, 8, 10]
target = 8
print(s.searchRange(nums, target))
