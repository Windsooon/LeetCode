class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        nums.sort()
        min_v = nums[0] + nums[1] + nums[2]
        for a, b in enumerate(nums[:-2]):
            c, d = a+1, len(nums)-1
            while c < d:
                sum = b + nums[c] + nums[d]
                if sum == target:
                    return target
                elif abs(target-sum) < abs(target-min_v):
                    min_v = sum
                    print(min_v)
                if sum > target:
                    d -= 1
                else:
                    c += 1
        return min_v

c = Solution()
c.threeSumClosest([1,1,1,0], 100)
