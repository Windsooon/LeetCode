class Solution(object):
    def longestConsecutive(self, nums):
        import pdb; pdb.set_trace()
        d, ans = {}, 0
        for n in nums:
            if n not in d:
                left = d[n-1] if n-1 in d else 0
                right = d[n+1] if n+1 in d else 0
                current = left+right+1
                d[n-left] = d[n+right] = d[n] = current
                ans = max(ans, current)
        return ans


s = Solution()
len = s.longestConsecutive([100, 1, 3, 2, 4, 200])
print(len)
