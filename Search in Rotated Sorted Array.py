class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if target > nums[mid]:
                if nums[mid] < nums[0] and target >= nums[0]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] >= nums[0] and target < nums[0]:
                    l = mid + 1
                else:
                    r = mid
        return -1


s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1,3], 3) == 1
assert s.search([3,5,1], 3) == 0
