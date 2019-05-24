class Solution:
    def search(self, nums, target):
        # [4,5,6,7,8,1,2,3], right = 7
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1,3], 3) == 1
assert s.search([3,5,1], 3) == 0
assert s.search([5,1,3], 3) == 2
assert s.search([4,5,6,7,8,1,2,3], 8) == 4
