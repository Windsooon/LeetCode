class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        first = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                first = i-1
                break
        if first == -1:
            nums.reverse()
        else:
            for i in range(len(nums)-1, first-1, -1):
                if nums[i] > nums[first]:
                    nums[i], nums[first] = nums[first], nums[i]
                    break
        nums = nums[:first+1] + nums[first+1:][::-1]

s = Solution()
# s.nextPermutation([1, 2, 3])
s.nextPermutation([1, 3, 2])
