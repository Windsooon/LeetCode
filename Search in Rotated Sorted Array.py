class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if target <= nums[right] and nums[mid] >= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] and nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1



s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1,3], 3) == 1
assert s.search([3,5,1], 3) == 0
assert s.search([5,1,3], 3) == 2
assert s.search([5,1,2,3,4], 1) == 1
assert s.search([4,5,6,7,8,1,2,3], 8) == 4
