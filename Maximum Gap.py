class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        gap = (max_val - min_val) // (len(nums)-1) or 1
        # 3, 6, 9, 1
        # [[], [], [], []]
        # breakpoint()
        lst = [[None, None] for i in range((max_val-min_val)//gap+1)]
        for n in nums:
            # [[1], [3], [6], [9]]
            bucket = lst[(n-min_val)//gap]
            bucket[0] = n if not bucket[0] else min(bucket[0], n)
            bucket[1] = n if not bucket[1] else max(bucket[1], n)
        max_gap = 0
        current_last = lst[0][-1]
        for i in range(len(lst)):
            if lst[i][0]:
                max_gap = max(max_gap, lst[i][0] - current_last)
                current_last = lst[i][-1]
        return max_gap


s = Solution()
assert (s.maximumGap([3, 6, 9, 1])) == 3
assert (s.maximumGap([10])) == 0
assert (s.maximumGap([1, 3, 100])) == 97
assert (s.maximumGap([3, 9, 21, 25, 29, 37, 43, 49])) == 12
assert (s.maximumGap([1, 1, 1, 1])) == 0
assert (s.maximumGap([100,3,2,1])) == 97
assert (s.maximumGap([1,1,1,1,1,5,5,5,5,5])) == 4

