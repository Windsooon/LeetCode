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

class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        return self.findTargetRecursion(nums, 0, S)

    def findTargetRecursion(self, nums, start, target):
        if start == len(nums)-1:
            if nums[start] == target == 0:
                return 2
            elif nums[start] == target or nums[start] == -target:
                return 1
            else:
                return 0
        plus = self.findTargetRecursion(nums, start+1, target+nums[start])
        minus = self.findTargetRecursion(nums, start+1, target-nums[start])
        return plus + minus

class Solution:
# dp[i][j] <- dp[i+1][target+nums[i]]
#          <- dp[i+1][target-nums[i]]
# -5  5 
# 10
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)
        if target > total_sum:
            return 0
        nums_range = 2 * total_sum + 1
        dp = [[0] * nums_range for i in range(len(nums))]
        dp[-1][nums[-1]+total_sum] += 1
        dp[-1][-nums[-1]+total_sum] += 1
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
        for i in range(len(nums)-2, -1, -1):
            for j in range(nums_range):
                # -15 -19 -11
                if 0 <= j+nums[i] < nums_range:
                    dp[i][j] += dp[i+1][j+nums[i]]
                if 0 <= j-nums[i] < nums_range:
                    dp[i][j] += dp[i+1][j-nums[i]]
        print(dp)
        return dp[0][target+total_sum]

import collections

class Solution:
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)
        if target > total_sum or target < -total_sum:
            return 0
        current = dict()
        if nums[-1] not in current:
            current[nums[-1]] = 1
        else:
            current[nums[-1]] += 1
        if -nums[-1] not in current:
            current[-nums[-1]] = 1
        else:
            current[-nums[-1]] += 1
        for i in range(len(nums)-2, -1, -1):
            tem = dict()
            # 4: 2
            for k, v in current.items():
                # 1 + 4
                if nums[i] + k not in tem:
                    tem[nums[i] + k] = 0
                    tem[nums[i] + k] += current[k]
                else:
                    tem[nums[i] + k] += current[k]
                # -1 + 4
                if -nums[i] + k not in tem:
                    tem[-nums[i] + k] = 0
                    tem[-nums[i] + k] += current[k]
                else:
                    tem[-nums[i] + k] += current[k]
            current = tem
        return 0 if target not in current else current[target]

s = Solution()
nums = [7,9,3,8,0,2,4,8,3,9]
S = 0
print(s.findTargetSumWays(nums, S))
