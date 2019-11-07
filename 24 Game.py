class Solution:
    def judgePoint24(self, nums):
        return self.dfs(nums)

    def dfs(self, nums):
        if len(nums) == 1:
            return round(nums, 2) == 24.00
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                first, second = nums[i], nums[j]
                can = [first+second, first-second, first*second, second-first]
                if first:
                    can.append(second/first)
                if second:
                    can.append(first/second)
                tem_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                for c in can:
                    if self.dfs(tem_nums + [c]):
                        return True
        return False
