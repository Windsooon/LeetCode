import bisect

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import pdb; pdb.set_trace()
        if nums is None or not nums: return []
        n = len(nums)
        res, newNums = [0] * n, []
        for i in range(n-1, -1, -1):
            idx = bisect.bisect_left(newNums, nums[i])
            newNums.insert(idx, nums[i])
            # bisect.insort_left(newNums, nums[i])
            res[i] = idx
        return res


s = Solution()
print(s.countSmaller([5, 2, 6, 1]))
