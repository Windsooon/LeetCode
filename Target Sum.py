class Solution:
    def findTargetSumWays(self, nums, S):
        if len(nums) == 0:
            return 0
        self.cache = dict()
        self.nums = nums
        return self.recursion(len(nums), S)

    def recursion(self, index, current):
        if (index, current) in self.cache:
            return self.cache[(index, current)]
        if len(nums[:index]) == 1:
            if nums[0] == current and -nums[0] == current:
                return 2
            elif nums[0] == current or -nums[0] == current:
                return 1
            else:
                return 0
        plus = self.recursion(index-1, current-nums[index-1])
        minus = self.recursion(index-1, current+nums[index-1])
        self.cache[(index, current)] = plus + minus
        return plus + minus

s = Solution()
nums = [43,1,49,22,41,1,11,1,24,10,26,49,33,4,20,19,44,42,2,37]
S = 17

print(s.findTargetSumWays(nums, S))
