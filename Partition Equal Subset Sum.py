import collections

#class Solution:
#    def canPartition(self, nums) -> bool:
#        total = sum(nums)
#        if total % 2 == 1:
#            return False
#        
#        half = total // 2
#        prev = set()
#        
#        dp = [[num] for num in nums]
#        
#        for i, num1 in enumerate(nums[1:], 1):
#            if num1 == half:
#                return True
#            if half - num1 in prev:
#                return True
#            prev.add(num1)
#            for num2 in dp[i-1]:
#                if num1 + num2 == half:
#                    return True
#                if num1 + num2 < half:
#                    dp[i].append(num1+num2)
#                    prev.add(num1+num2)
#        return False

class Solution:
    def __init__(self):
        self.count = 0
    def canFindSum(self, nums, target, ind, n, d):
        self.count += 1
        if target in d: return d[target]
        if target == 0: d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in range(ind, n):
                    if self.canFindSum(nums, target - nums[i], i+1, n, d):
                        d[target] = True
                        break
        return d[target]
    
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        ans = self.canFindSum(nums, s/2, 0, len(nums), {})
        print(self.count)
        return ans

class Solution:
    def canPartition(self, nums):
        # [1, 5, 11, 5]
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        # 11
        target = sum_nums // 2
        # [False] * 12
        if nums[-1] == target:
            return True
        if max(nums) > target:
            return False
        dp = [False] * (target+1)
        dp[0] = True
        dp[nums[-1]] = True
        # 2
        for i in range(len(nums)-2, -1, -1):
            for j in range(target, -1, -1):
                if j == target:
                    if dp[j] or dp[j-nums[i]]:
                        return True
                elif j < nums[i]:
                    dp[j] = False
                else:
                    dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]

class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        if self.dfs(0, nums, total_sum // 2):
            return True
        return False
    
    def dfs(self, start, nums, target):
        if target == 0:
            return True
        if start == len(nums):
            return False
        for i in range(start+1, len(nums)+1):
            if target-nums[start] >= 0:
                if self.dfs(i, nums, target-nums[start]):
                    return True
        return False

s = Solution()
# nums = [20,68,68,11,48,18,50,5,3,51,52,11,13,11,38,100,30,87,1,56,85,63,14,96,7,17,54,11,32,61,94,13,85,10,78,57,69,92,66,28,70,20,3,29,10,73,89,86,28,48,69,54,87,11,91,32,59,4,88,20,81,100,29,75,79,82,6,74,66,30,9,6,83,54,54,53,80,94,64,77,22,7,22,26,12,31,23,26,65,65,35,36,34,1,12,44,22,73,59,99]
# nums = [20,68,68,11,48,18,50,5,3,51,52,11,13,11,38,100,30,87,1]
nums = [1,5,11,5]
assert s.canPartition(nums) is True
nums = [1,2,5]
assert s.canPartition(nums) is False
nums = [1,3,5,5,5,5]
assert s.canPartition(nums) is False
