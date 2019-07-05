class Solution:
    def splitArray(self, nums, m):
        # base case
        if m == 1 or not nums:
            return sum(nums)
        # create the first row answer which is sum of the pre elements
        l = max(nums)
        r = sum(nums)+1
        while l < r:
            mid = (r+l)//2
            if self.valid(mid, nums, m):
                l = mid + 1
            else:
                r = mid
        return l

    def valid(self, target, nums, m):
        count = 0
        tem_sum = 0
        i = 0
        while i < len(nums):
            if tem_sum + nums[i] > target:
                tem_sum = 0
                count += 1
                i -= 1
                if count >= m:
                    return True
            else:
                tem_sum += nums[i]
            i += 1
        return False


s = Solution()
nums = [7,2,5,10,8]
m = 2
print(s.splitArray(nums, m))
