# class Solution:
#     def findMin(self, nums):
#         if not nums:
#             return
#         left, right = 0, len(nums)-1
#         if nums[left] < nums[right]:
#             return nums[left]
#         while left < right:
#             mid = (left+right)//2
#             if nums[mid] < nums[right]:
#                 right = mid - 1
#             elif nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right -= 1
#         return nums[mid]
# 
# s = Solution()
# print(s.findMin([1, 1, 1, 0, 1]))

class Solution:
    def binarysearch(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1


s = Solution()
print(s.binarysearch([1,2,4,6,12,44,123], 123))
print(s.binarysearch([1,2,4,6,12,44,123], 6))
print(s.binarysearch([1,2,4,6,12,44,123], 12))
print(s.binarysearch([1,2,4,6,12,44,123], 13))
