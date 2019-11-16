class Solution:
    def threeSumSmaller(self, nums, target):
        count = 0
        nums.sort()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    count += k-j
                    j += 1
                else:
                    k -= 1
        return count
