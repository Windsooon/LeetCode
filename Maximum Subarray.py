class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return
        dp = [0] * len(nums)
        output = float('-inf')
        dp[0] = nums[0]
        for i in range(1, len(dp)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
                if dp[i] > output:
                    output = dp[i]
        return output

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))
