class Solution:
    def findUnsortedSubarray(self, nums):
        if len(nums) < 2:
            return 0
        left = 0
        right = len(nums)-1
        

s = Solution()
# print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray([1,2,3,4,5]))
