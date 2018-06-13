class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        count = 1
        for n in nums[1:]:
            if n == min_val:
                count += 1
            else:
                count -= 1
            if count < 0:
                min_val = n
                count = 1
        return min_val

s = Solution()
nums = [3, 2, 3]
nums2 = [3, 2, 2, 3, 2]
nums3 = [3, 1, 1, 3, 3]
print(s.majorityElement(nums))
print(s.majorityElement(nums2))
print(s.majorityElement(nums3))
