class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        base = length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                base += 1
            else:
                base = 1
            length = max(length, base)
        return length

s = Solution()
a = [1, 3, 5, 4, 2, 3, 4, 5]
b = [1, 3, 5, 7]
c = [1, 3, 2, 4, 6]
print(s.findLengthOfLCIS(a))
print(s.findLengthOfLCIS(b))
print(s.findLengthOfLCIS(c))
