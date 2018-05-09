class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
    
k = [2, 1]
s = Solution()
s.singleNumber(k)
