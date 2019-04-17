class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        k = []
        nums.sort()
        for i in range(len(nums)):
            t = target - nums[i]
            for l in range(i+1, len(nums)):
                t2 = t - nums[l]
                left = l + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == t2:
                        if ([nums[i], nums[l], nums[left], nums[right]]) not in k:
                            k.append([nums[i], nums[l], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < t2:
                        left += 1
                    else:
                        right -= 1
        return k

a = Solution()
print(a.fourSum([1, 0, -1, 0, -2, 2], 0))
