class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        min_val, cur, first, second = float('inf'), 0, 0, 0
        while second <= len(nums)-1 and first <= second:
            cur += nums[second]
            while cur >= s:
                min_val = min(min_val, second-first+1)
                cur -= nums[first]
                first += 1
            else:
                second += 1
        return min_val if min_val != float('inf') else 0


s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(3, [1,1]))
