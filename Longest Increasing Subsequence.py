class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) < 2:
            return len(nums)
        dp = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)



arr = [10,9,2,5,3,7,101,18]
arr = [2, 2]
s = Solution()
print(s.lengthOfLIS(arr))
