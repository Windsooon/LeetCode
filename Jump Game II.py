class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [2,3,1,1,4]
        if len(nums) <= 2:
            return 0
        current = [0]
        level = 0
        # 0 < 4
        # import pdb; pdb.set_trace()
        while(max(current) < len(nums)-1):
            max_val = 0
            for c in current:
                # max_val = max(0, 0 + 2)
                max_val = max(max_val, c+nums[c])
            current = list(range(current[-1]+1, max_val+1))
            level += 1
        return level

# nums = [4,1,1,3,1,1,1]
# nums = [1,2,1,1,1]
# nums = [2,3,1,1,4]
s = Solution()
print(s.jump(nums))

