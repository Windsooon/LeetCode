class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # breakpoint()
        if (len(nums) < 2):
             return 0
        current_max = 0
        step = 0
        max_index = 0
        for i in range(len(nums)):
            max_index = max(max_index, nums[i]+i)
            if max_index >= len(nums)-1:
                return step + 1
            if i == current_max:
                step += 1
                current_max = max_index
        return step





# nums = [4,1,1,3,1,1,1]
# nums = [1,2,3]
# nums4 = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]
nums4 = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,3,3]
nums3 = [4,1,1,3,1,1,1]
nums2 = [2,3,1,1,4]
nums = [2, 1]
s = Solution()
# assert (s.jump(nums)) == 0
assert (s.jump(nums2)) == 2
assert (s.jump(nums3)) == 2
assert (s.jump(nums)) == 1
print(s.jump(nums4))

